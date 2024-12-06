from flask import Blueprint, jsonify
from backend.models.tTipoPieza import TTipoPieza

id_tipo = Blueprint('id_tipo', __name__)

@id_tipo.route('/id_tipo', methods=['GET'])
def obtener_tipos():
    tipos = TTipoPieza.query.all()
    return jsonify([{"Id_tipo": tipo.id_tipo, "Nombre": tipo.nombre} for tipo in tipos]), 200