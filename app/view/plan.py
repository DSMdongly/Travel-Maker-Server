from app.doc.plan import CREATE_SPEC, UPDATE_SPEC, LIST_SPEC, DELETE_SPEC
from app.model import User, Plan

from flask import abort, Blueprint, request, jsonify
from flask_jwt_extended import *

from flasgger import swag_from


api = Blueprint(__name__, 'place_api')


@api.route('/plan/new', methods=['POST'])
@swag_from(CREATE_SPEC)
@jwt_required
def create():
    form = request.form
    files = request.files

    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)

    if not user:
        return (
            jsonify(reason='사용자를 조회할 수 없음. 토큰을 재발급 받아야 함'),
            400,
        )

    title = form.get('title')
    category = int(form.get('category', Plan.Category.ETC))
    location = form.get('location')
    location = location and int(location)
    description = form.get('description')
    schedules = form.get('schedules')
    price = form.get('price', 0)
    price = price and int(price)

    plan = Plan(
        user_id=user_id,
        title=title,
        description=description,
        location=location,
        category=category,
        schedules=schedules,
        price=price,
    )

    plan.save()

    return (
        jsonify(
            created={
                'id': plan.id,
                'title': title,
                'user_id': user_id,
                'description': description,
                'location': location,
                'location_name': Plan.get_location_name(location),
                'category': category,
                'category_name': Plan.get_category_name(category),
                'schedules': schedules,
                'price': price,
            }
        )
    )


@api.route('/plan/list', methods=['GET'])
@swag_from(LIST_SPEC)
def list():
    args = request.args
    plans = Plan.query

    title = args.get('title')
    category = args.get('category')
    location = args.get('location')
    user_id = args.get('user_id')
    price_range = args.get('price_range')

    if title:
        plans = plans.filter(Plan.title.like('%' + title + '%'))
    if category is not None:
        plans = plans.filter_by(category=int(category))
    if location:
        plans = plans.filter_by(location=int(location))
    if user_id:
        plans = plans.filter_by(user_id=user_id)

    if price_range:
        price_ranges = price_range.split(',')
        if len(price_ranges) == 1:
            plans = plans.filter(Plan.price / int(price_ranges[0]) == 1)
        if len(price_ranges) == 2:
            plans = plans.filter(Plan.price >= int(price_ranges[0]))
            plans = plans.filter(Plan.price <= int(price_ranges[1]))

    plans = plans.order_by(Plan.id.desc()).all()

    return (
        jsonify(
            plans=[
                plan.to_dict() for plan in plans
            ]
        )
    )


@api.route('/plan/update', methods=['PUT'])
@swag_from(UPDATE_SPEC)
@jwt_required
def update():
    form = request.form

    title = form.get('title')
    description = form.get('description')
    category = int(form.get('category', '0'))
    location = form.get('location')
    location = location and int(location)
    schedules = form.get('shcedules')
    price = form.get('price', 0)
    price = price and int(price)

    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)

    if not user:
        return (
            jsonify(reason='사용자를 조회할 수 없음. 토큰을 재발급 받아야 함'),
            400
        )

    plan_id = form.get('plan_id')
    plan = Plan.find_by_id(plan_id)

    if not plan:
        return (
            jsonify(reason='해당 id에 대응하는 plan이 없음. plan_id 값을 확인해야 함'),
            400
        )

    plan.update(
        title=title or plan.title,
        description=description or plan.description,
        category=category or plan.category,
        locatoin=location or plan.location,
        schedules=schedules or plan.schedules,
        price=price or plan.price,
    )

    return jsonify(
        updated={
            'id': plan.id,
            'title': plan.title,
            'user_id': plan.user_id,
            'description': plan.description,
            'location': plan.location,
            'location_name': Plan.get_location_name(plan.location),
            'category': plan.category,
            'category_name': Plan.get_category_name(plan.category),
            'schedules': plan.schedules,
            'price': plan.price,
        },
    )


@api.route('/plan/delete', methods=['DELETE'])
@swag_from(DELETE_SPEC)
@jwt_required
def delete():
    form = request.form

    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)

    if not user:
        return (
            jsonify(reason='사용자를 조회할 수 없음. 토큰을 재발급 받아야 함'),
            400
        )

    plan_id = form.get('plan_id')
    plan_id = plan_id and int(plan_id)
    plan = Plan.find_by_id(plan_id)

    if not plan:
        return (
            jsonify(reason='해당 id에 대응하는 plan이 없음. plan_id 값을 확인해야 함'),
            400
        )

    if plan.user_id != user.id:
        return (
            jsonify(reason='해당 사용자만 삭제가 가능합니다.'),
            403,
        )

    plan.remove()

    return jsonify(
        deleted={
            'id': plan_id,
        },
    )

