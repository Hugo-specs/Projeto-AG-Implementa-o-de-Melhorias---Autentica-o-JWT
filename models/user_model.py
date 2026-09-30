import sqlite3
from database.db import get_db_connection


class UserModel:

    @staticmethod
    def find_by_username(username):
        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        conn.close()
        return user

    @staticmethod
    def find_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute(
            'SELECT id, username, password FROM user WHERE id = ?', (user_id,)
        ).fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def create_user(username, password):
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, password)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def update_user(user_id, username, password):
        """True = atualizou, False = não existe, None = username duplicado."""
        conn = get_db_connection()
        try:
            cur = conn.execute(
                'UPDATE user SET username = ?, password = ? WHERE id = ?',
                (username, password, user_id)
            )
            conn.commit()
            return cur.rowcount > 0
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        try:
            cur = conn.execute('DELETE FROM user WHERE id = ?', (user_id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            conn.close()
