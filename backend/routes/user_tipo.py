from flask import Blueprint, jsonify, request
from backend.models.tUsuario import Usuario

auth = Blueprint('UsuarioTipo', __name__)

@auth.route('/user_tipo/admin', methods=['POST'])
def es_admin():
    try:
        data = request.get_json()
        nombre_usuario = data.get("nombre")
        usuario = Usuario.query.filter_by(nombre=nombre_usuario).first()

        if usuario and usuario.rolName == "admin":
            return jsonify({"message": "Usuario es admin, acción habilitada"}), 200  # Cambié el código a 200
        else:
            return jsonify({"message": "Usuario NO es admin, acción deshabilitada"}), 403  # Cambié el código a 403
    except Exception as e:
        return jsonify({"message": f"Error en el servidor: {str(e)}"}), 500
