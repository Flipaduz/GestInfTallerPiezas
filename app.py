from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@localhost/TrabajoGI2425?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class TPiezas(db.Model):
    __tablename__ = 'tPiezas'  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255))
    fabricante = db.Column(db.String(255))
    id_tipo = db.Column(db.String(4))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fabricante": self.fabricante,
            "id_tipo": self.id_tipo
        }
    
@app.route('/piezas', methods=['GET'])
def get_piezas():
    piezas = TPiezas.query.all()
    return jsonify([pieza.to_dict() for pieza in piezas])

if __name__ == '__main__':
    app.run(debug = True)