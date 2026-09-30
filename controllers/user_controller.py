from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models.user_model import UserModel


class UserController:

    @staticmethod
    def register_user(data):
        data = data or {}
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"}, 400

        hashed_password = generate_password_hash(password)

        if UserModel.create_user(username, hashed_password):
            return {"message": "Usuário registrado com sucesso"}, 201

        return {"error": "Nome de usuário já existe"}, 400

    @staticmethod
    def login_user(data):
        data = data or {}
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {"error": "Nome de usuário e senha são obrigatórios"}, 400

        user = UserModel.find_by_username(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']))
            return {"access_token": access_token}, 200

        return {"error": "Nome de usuário ou senha inválidos"}, 401

    @staticmethod
    def get_user(user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"error": "Usuário não encontrado"}, 404
        # nunca devolver o hash da senha
        return {"id": user['id'], "username": user['username']}, 200

    @staticmethod
    def update_user(user_id, data):
        data = data or {}
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"error": "Usuário não encontrado"}, 404

        username = data.get('username')
        password = data.get('password')

        if not username and not password:
            return {"error": "Informe username e/ou password para atualizar"}, 400

        # campos não enviados mantêm o valor atual
        new_username = username or user['username']
        new_password = generate_password_hash(password) if password else user['password']

        result = UserModel.update_user(user_id, new_username, new_password)
        if result is None:
            return {"error": "Nome de usuário já existe"}, 400
        if result is False:
            return {"error": "Usuário não encontrado"}, 404
        return {"message": "Usuário atualizado com sucesso"}, 200

    @staticmethod
    def delete_user(user_id):
        if UserModel.delete_user(user_id):
            return {"message": "Usuário excluído com sucesso"}, 200
        return {"error": "Usuário não encontrado"}, 404
