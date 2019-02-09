from app.model import User

from flask import abort, Blueprint, request, jsonify
from flask_jwt_extended import *


api = Blueprint(__name__, 'place_api')


@fresh_jwt_required
def create():
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)

    if not user:
        return jsonify()
    form = request.form
    files = request.files

    image = files.get('image')
    title = form.get('title')
    description = form.get('description')
    plan_id = form.get('plan_id')



