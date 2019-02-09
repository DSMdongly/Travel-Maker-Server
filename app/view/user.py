from flask import abort, Blueprint, request, jsonify
from flask_jwt_extended import *
from flasgger import swag_from
from app.doc.user import PROFILE_SHOW_SPEC, PROFILE_UPDATE_SPEC
from app.model import User

api = Blueprint(__name__, 'user_api')


def _get_user_dict(user):
    return {
        'id': user.id,
        'name': user.name,
        'descritpion': user.description,
        'phone': user.phone,
        'email': user.email,
        'keywords': user.keywords,
    }


@api.route('/user/profile/show', methods=['GET'])
@swag_from(PROFILE_SHOW_SPEC)
@jwt_required
def profile_show():
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)

    if not user:
        return (
            jsonify(reason='사용자를 조회할 수 없음. 액세스 토큰을 재발급 받아야 함'),
            400,
        )

    return jsonify(
        profile=_get_user_dict(user),
    )


@api.route('/user/profile/update', methods=['PUT'])
@swag_from(PROFILE_UPDATE_SPEC)
@jwt_required
def profile_update():
    form = request.form

    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)

    if not user:
        return (
            jsonify(reason='사용자를 조회할 수 없음. 액세스 토큰을 재발급 받아야 함'),
            400,
        )

    name = form.get('form')
    description = form.get('description')
    phone = form.get('phone')
    email = form.get('email')
    keywords = form.get('keywords')

    user.update(
        name=name or user.name,
        description=description or user.description,
        phone=phone or user.phone,
        email=email or user.email,
        keywords=keywords or user.keywords,
    )

    return jsonify(
        updated=_get_user_dict(user)
    )
