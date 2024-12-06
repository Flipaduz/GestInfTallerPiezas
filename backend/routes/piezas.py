from flask import Blueprint, jsonify
from backend.models.tPiezas import TPiezas

piezas_bp = Blueprint('piezas', __name__)

@piezas_bp.route('/piezas', methods=['GET'])
def get_piezas():
    piezas = TPiezas.query.all()
    return jsonify([{"id": p.id, "nombre": p.nombre, "descripcion": p.descripcion} for p in piezas])