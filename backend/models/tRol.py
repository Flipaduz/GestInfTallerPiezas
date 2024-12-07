from backend.app import db

class TRol(db.Model):
    __tablename__ = 'tRol'
    rolName = db.Column(db.String(50), primary_key=True)
    rolDes = db.Column(db.String(255), nullable=True)
    admin = db.Column(db.Boolean, nullable=False)

    permisos = db.relationship('TPermiso', back_populates='rol', cascade="all, delete-orphan")
    usuarios = db.relationship('TUsuario', back_populates='rol')