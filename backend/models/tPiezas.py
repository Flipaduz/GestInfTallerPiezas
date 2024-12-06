from sqlalchemy import Column, Integer, String
from backend.app import db

class TPiezas(db.Model):
    __tablename__ = 'tPiezas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))