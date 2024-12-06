from flask import Blueprint, jsonify
from backend.models.tPiezas import TPiezas

piezas_bp = Blueprint('piezas', __name__)

@piezas_bp.route('/piezas/<tipo_id>', methods=['GET'])
def obtener_piezas_por_tipo(tipo_id):
    try:
        # Consultar las piezas asociadas al tipo
        piezas = TPiezas.query.filter_by(id_tipo=tipo_id).all()
        if not piezas:
            return jsonify({"message": "No se encontraron piezas para este tipo."}), 404

        # Serializar los resultados
        piezas_serializadas = [
            {"id": pieza.id, "nombre": pieza.nombre, "fabricante": pieza.fabricante, "id_tipo": pieza.id_tipo}
            for pieza in piezas
        ]
        return jsonify(piezas_serializadas), 200

    except Exception as e:
        return jsonify({"message": f"Error al obtener piezas: {str(e)}"}), 500