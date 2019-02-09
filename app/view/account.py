from flask import abort, Blueprint, request, jsonify
from flask_jwt_extended import *
from flasgger import swag_from
from app.doc.account import REGISTER_SPEC, AUTH_LOCAL_SPEC, AUTH_SOCIAL_SPEC
from app.model import User, UserSocialLogin
from app.libs import facebook

api = Blueprint(__name__, 'account_api')


@swag_from(AUTH_LOCAL_SPEC)
@api.route('/auth/local', methods=['POST'])
def local_auth():
    payload = request.form or request.json

    id = payload['id']
    password = payload['password']

    user = User.find_by_id(id)

    if not (user and password == user.password):
        return (
            jsonify(
                reason='아이디 혹은 패스워드가 일치하지 않습니다.'
            ),
            401,
        )

    return jsonify(
        access_token=create_access_token(identity=id),
        refresh_token=create_refresh_token(identity=id),
    )


@swag_from(AUTH_SOCIAL_SPEC)
@api.route('/auth/social', methods=['POST'])
def social_auth():
    payload = request.form or request.json

    social_api_token = payload.get('social_api_token')
    login_method = payload.get('login_method', 'facebook')

    api_user_data = _get_social_api_user_data(
        login_method,
        social_api_token,
    )

    if not api_user_data:
        return (
            jsonify(reason='Social API 로그인 실패, social_api_token 값을 확인해주세요'),
            400,
        )

    api_id = api_user_data.get('id')
    user_social_login = UserSocialLogin.find_by_api_id_and_kind(api_id, login_method)

    if not user_social_login:
        return (
            jsonify(reason='소셜 계정이 서버에 등록되지 않았습니다. 소셜 회원가입을 진행해주세요'),
            401,
        )

    return jsonify(
        access_token=create_access_token(identity=user_social_login.user_id),
        refresh_token=create_refresh_token(identity=user_social_login.user_id),
    )


def _get_social_api_user_data(api_kind, api_token):
    user_data = {}

    if api_kind == UserSocialLogin.ApiKind.FACEBOOK:
        user_data = facebook.get_user_data(api_token)

    return user_data


@swag_from(REGISTER_SPEC)
@api.route('/register', methods=['POST'])
def register():
    payload = request.form or request.json

    id = payload.get('id')
    password = payload.get('password')
    name = payload.get('name')
    phone = payload.get('phone')
    email = payload.get('email')

    user = User(
        id=id,
        name=name,
        password=password,
        phone=phone,
        email=email,
    )

    user.save()
    join_method = payload.get('join_method', 'local')

    if join_method != 'local':
        social_api_token = payload['social_api_token']

        _add_user_social_login(
            user.id,
            join_method,
            social_api_token,
        )

    return (
        jsonify(
            access_token=create_access_token(identity=id),
            refresh_token=create_refresh_token(identity=id),
        ), 201
    )


def _add_user_social_login(uid, join_method, api_token):
    user_data = _get_social_api_user_data(join_method, api_token)

    if not user_data:
        return

    api_id = user_data.get('id')

    user_social_login = UserSocialLogin(
        user_id=uid,
        api_id=api_id,
        api_kind=join_method,
    )

    user_social_login.save()


@swag_from()
@api.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    return {
        'access_token': create_access_token(identity=get_jwt_identity()),
    }
