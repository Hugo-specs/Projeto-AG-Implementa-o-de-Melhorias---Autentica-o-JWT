from models.formulario_model import FormularioModel

CAMPOS = ('nome', 'email', 'data_nascimento', 'cpf', 'genero')


def _extrair_campos(data):
    data = data or {}
    return [data.get(c) for c in CAMPOS]


class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        valores = _extrair_campos(data)
        if not all(valores):
            return {"error": "Todos os campos são obrigatórios"}, 400

        if FormularioModel.create_formulario(user_id, *valores):
            return {"message": "Formulário criado com sucesso"}, 201
        return {"error": "Erro ao criar formulário"}, 500

    @staticmethod
    def get_formulario(formulario_id):
        formulario = FormularioModel.find_by_id(formulario_id)
        if not formulario:
            return {"error": "Formulário não encontrado"}, 404
        return formulario, 200

    @staticmethod
    def update_formulario(formulario_id, data):
        if not FormularioModel.find_by_id(formulario_id):
            return {"error": "Formulário não encontrado"}, 404

        valores = _extrair_campos(data)
        if not all(valores):
            return {"error": "Todos os campos são obrigatórios"}, 400

        if FormularioModel.update_formulario(formulario_id, *valores):
            return {"message": "Formulário atualizado com sucesso"}, 200
        return {"error": "Erro ao atualizar formulário"}, 500

    @staticmethod
    def delete_formulario(formulario_id):
        if FormularioModel.delete_formulario(formulario_id):
            return {"message": "Formulário excluído com sucesso"}, 200
        return {"error": "Formulário não encontrado"}, 404
