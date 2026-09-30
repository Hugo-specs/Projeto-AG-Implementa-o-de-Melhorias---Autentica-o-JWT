import sqlite3
from database.db import get_db_connection


class FormularioModel:

    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            conn.execute(
                '''INSERT INTO formulario
                   (user_id, nome, email, data_nascimento, cpf, genero)
                   VALUES (?, ?, ?, ?, ?, ?)''',
                (user_id, nome, email, data_nascimento, cpf, genero)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def find_by_id(formulario_id):
        conn = get_db_connection()
        row = conn.execute(
            'SELECT * FROM formulario WHERE id = ?', (formulario_id,)
        ).fetchone()
        conn.close()
        return dict(row) if row else None

    @staticmethod
    def update_formulario(formulario_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()
        try:
            cur = conn.execute(
                '''UPDATE formulario
                   SET nome = ?, email = ?, data_nascimento = ?, cpf = ?, genero = ?
                   WHERE id = ?''',
                (nome, email, data_nascimento, cpf, genero, formulario_id)
            )
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def delete_formulario(formulario_id):
        conn = get_db_connection()
        try:
            cur = conn.execute(
                'DELETE FROM formulario WHERE id = ?', (formulario_id,)
            )
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()
