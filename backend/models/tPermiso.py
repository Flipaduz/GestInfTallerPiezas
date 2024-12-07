from backend.app import db
from sqlalchemy import PrimaryKeyConstraint

class TPermiso(db.Model):
    __tablename__ = 'tPermiso'
    rolName = db.Column(db.String(50), db.ForeignKey('tRol.rolName'), nullable=False)
    pantalla = db.Column(db.String(50), nullable=False)
    acceso = db.Column(db.Boolean, nullable=False)
    modificacion = db.Column(db.Boolean, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('rolName', 'pantalla'),
    )

    rol = db.relationship('TRol', back_populates='permisos')