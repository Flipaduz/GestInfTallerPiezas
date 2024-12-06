from backend.app import db

class TTipoPieza(db.Model):
    __tablename__ = 'tTipoPieza'
    id_tipo = db.Column(db.String(4), primary_key=True)
    nombre = db.Column(db.String(80))

    def to_dict(self):
        return {"id_tipo": self.id_tipo, "nombre": self.nombre}