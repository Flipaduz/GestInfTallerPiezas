from flask_sqlalchemy import SQLAlchemy
from backend.app import db

class Usuario(db.Model):
    __tablename__ = 'tUsuario'  # Nombre de la tabla en la base de datos

    nombre = db.Column(db.String(50), primary_key=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    rolName = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.usuario}>'

    @classmethod
    def validar_usuario(cls, user, pw):
        # Este método consulta la base de datos para ver si el usuario y la contraseña coinciden
        usuario_obj = cls.query.filter_by(nombre=user, password=pw).first()
        return usuario_obj is not None