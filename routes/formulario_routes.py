from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.formulario_controllers import FormularioController

formulario_bp = Blueprint('formularios', __name__)


def _resp(result):
    body, status = result
    return jsonify(body), status


# POST 
@formulario_bp.route('/', methods=['POST'], strict_slashes=False)
@jwt_required()
def create_formulario():
    user_id = int(get_jwt_identity())
    return _resp(FormularioController.create_formulario(user_id, request.get_json(silent=True)))


# GET 
@formulario_bp.route('/<int:formulario_id>', methods=['GET'])
@jwt_required()
def get_formulario(formulario_id):
    return _resp(FormularioController.get_formulario(formulario_id))


# PUT 
@formulario_bp.route('/<int:formulario_id>', methods=['PUT'])
@jwt_required()
def update_formulario(formulario_id):
    return _resp(FormularioController.update_formulario(formulario_id, request.get_json(silent=True)))


# DELETE 
@formulario_bp.route('/<int:formulario_id>', methods=['DELETE'])
@jwt_required()
def delete_formulario(formulario_id):
    return _resp(FormularioController.delete_formulario(formulario_id))
