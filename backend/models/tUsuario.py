from backend.app import db

class TUsuario(db.Model):
    __tablename__ = 'tUsuario'  # Nombre de la tabla en la base de datos

    nombre = db.Column(db.String(50), primary_key=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    rolName = db.Column(db.String(50), db.ForeignKey('tRol.rolName'), nullable=False)

    rol = db.relationship('TRol', back_populates='usuarios')
   
    # Como si fuera un toString()
    def __repr__(self):
        return f'<Usuario {self.usuario}>'

