from backend.app import db

class TUsuario(db.Model):
    __tablename__ = 'tUsuario'  # Nombre de la tabla en la base de datos

    nombre = db.Column(db.String(50), primary_key=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    rolName = db.Column(db.String(50), db.ForeignKey('tRol.rolName'), nullable=False)

    rol = db.relationship('TRol', back_populates='usuarios')

    def __repr__(self):
        return f'<Usuario {self.usuario}>'

    @classmethod
    def validar_usuario(cls, user, pw):
        # Este método consulta la base de datos para ver si el usuario y la contraseña coinciden
        usuario_obj = cls.query.filter_by(nombre=user, password=pw).first()
        return usuario_obj is not None

    @classmethod
    def es_admin(cls, nombre):
        # Método que devuelve True si el usuario es administrador, False en caso contrario
        usuario = cls.query.filter_by(nombre=nombre).first()
        return usuario is not None and usuario.rolName == "administrador"