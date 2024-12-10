from backend.app import db

class TPiezas(db.Model):
    __tablename__ = 'tPiezas'
    id = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(255))
    fabricante = db.Column(db.String(255))
    id_tipo = db.Column(db.String(4))

    #Devuelve diccionario con los datos
    def to_dict(self):
        return {'id': self.id, 'nombre': self.nombre, 'fabricante': self.fabricante, "id_tipo": self.id_tipo}