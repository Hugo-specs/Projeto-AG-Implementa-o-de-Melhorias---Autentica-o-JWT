from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)


def _resp(result):
    body, status = result
    return jsonify(body), status


# POST /users/  (cadastro, sem JWT) - /users/register também funciona
@user_bp.route('/', methods=['POST'], strict_slashes=False)
@user_bp.route('/register', methods=['POST'])
def register():
    return _resp(UserController.register_user(request.get_json(silent=True)))


# POST /users/login
@user_bp.route('/login', methods=['POST'])
def login():
    return _resp(UserController.login_user(request.get_json(silent=True)))


# GET /users/<id>
@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return _resp(UserController.get_user(user_id))


# PUT /users/<id>
@user_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    return _resp(UserController.update_user(user_id, request.get_json(silent=True)))


# DELETE /users/<id>
@user_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return _resp(UserController.delete_user(user_id))
