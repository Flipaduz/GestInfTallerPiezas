from flask import Blueprint, request, jsonify
from backend.models.tUsuario import Usuario

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    try:
        # Obtener los datos del usuario desde la solicitud POST
        data = request.get_json()
        user = data.get('usuario')
        password = data.get('password')

        # Validar usuario
        if not user or not password:
            return jsonify({"message": "Usuario y contraseña son requeridos"}), 400

        # Usar el modelo Usuario para validar las credenciales
        if Usuario.validar_usuario(user, password):
            return jsonify({"message": "Login exitoso"}), 200
        else:
            return jsonify({"message": "Usuario o contraseña incorrectos"}), 401
    except Exception as e:
        return jsonify({"message": f"Error en el servidor: {str(e)}"}), 500