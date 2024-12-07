from flask import Blueprint, jsonify, request
from backend.models.tPiezas import TPiezas
from backend.app import db

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
    
@piezas_bp.route('/piezas/insertar', methods=['POST'])
def insertar_pieza():
    try:
        data = request.get_json()
        nombre = data.get("nombre")
        fabricante = data.get("fabricante")
        id_tipo = data.get("id_tipo")

        if not nombre or not fabricante or not id_tipo:
            return jsonify({"message": "Faltan datos"}), 400
        
        nueva_pieza = TPiezas(nombre = nombre, fabricante = fabricante, id_tipo = id_tipo)

        db.session.add(nueva_pieza)
        db.session.commit()

        return jsonify({"message": "Pieza añadida correctamente"}), 201
    except Exception as e:
        return jsonify({"message": f"Error al agregar la pieza: {str(e)}"}), 500
    
@piezas_bp.route('/piezas/actualizar/<int:id_pieza>', methods=['PUT'])
def actualizar_pieza(id_pieza):
    try:
        data = request.get_json()
        nombre = data.get("nombre")
        fabricante = data.get("fabricante")
        
        if not nombre or not fabricante:
            return jsonify({"message": "Faltan datos"}), 400
        
        pieza = TPiezas.query.get(id_pieza)

        if not pieza:
            return jsonify({"message": "Pieza no encontrada"}), 400
        
        pieza.nombre = nombre
        pieza.fabricante = fabricante
        db.session.commit()
        return jsonify({"message": "Pieza actualizada correctamente"}), 201
    except Exception as e:
        return jsonify({"message": f"Error al agregar la pieza: {str(e)}"}), 500

@piezas_bp.route('/piezas/borrar/<int:id_pieza>', methods=['DELETE'])
def borrar_pieza(id_pieza):
    try:
        pieza = TPiezas.query.get(id_pieza)

        if not pieza:
            return jsonify({"message": "Pieza no encontrada"}), 400
        db.session.delete(pieza)
        db.session.commit()
        return jsonify({"message": "Pieza borrada correctamente"}), 201
    except Exception as e:
        return jsonify({"message": f"Error al agregar la pieza: {str(e)}"}), 500