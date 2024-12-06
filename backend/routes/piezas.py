from flask import Blueprint
from backend.models.tPiezas import TPiezas

piezas_bp = Blueprint('piezas', __name__)

@piezas_bp.route('/piezas', methods=['GET'])
def obtener_piezas():
    piezas = TPiezas.query.all()
    return {'piezas': [pieza.to_dict() for pieza in piezas]}