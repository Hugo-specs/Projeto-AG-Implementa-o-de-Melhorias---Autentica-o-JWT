from flask import Flask
from flask_jwt_extended import JWTManager
from database.db import init_db
from routes.user_routes import user_bp
from routes.formulario_routes import formulario_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

jwt = JWTManager(app)

init_db()

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(formulario_bp, url_prefix='/formularios')

if __name__ == '__main__':
    app.run(debug=True)
