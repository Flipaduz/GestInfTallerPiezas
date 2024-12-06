import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@localhost/TrabajoGI2425?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Registrar rutas
    from backend.routes.piezas import piezas_bp
    from backend.routes.login import auth
    from backend.routes.id_tipo import id_tipo
    app.register_blueprint(piezas_bp)
    app.register_blueprint(auth)
    app.register_blueprint(id_tipo)

    return app