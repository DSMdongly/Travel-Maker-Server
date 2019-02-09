from flask import abort, Blueprint, request, jsonify
from flask_jwt_extended import *


api = Blueprint(__name__, 'place_api')


@fresh_jwt_required
def create():
    payload = request.form
    files = request.files

    image = files.get('image')
    title = payload.get('title')
    description = payload.get('description')
    pass
