from flask import Blueprint, request, jsonify
from backend.models.tUsuario import TUsuario
from backend.models.tRol import TRol
from backend.models.tPermiso import TPermiso

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    try:
        # Obtener los datos del usuario desde la solicitud POST
        data = request.get_json()
        user = data.get('usuario')
        password = data.get('password')
        pantalla = data.get('pantalla')

        # Validar usuario
        if not user or not password:
            return jsonify({"message": "Usuario y contraseña son requeridos"}), 400

        usuario_obj = TUsuario.query.filter_by(nombre=user, password=password).first()

        # Usar el modelo Usuario para validar las credenciales
        if not usuario_obj:
            return jsonify({"message": "Usuario o contraseña incorrectos"}), 401

        print("JUSTO ANTES DEL PRIMER QUERY")

        # Obtener rol del usuario
        rol_name = usuario_obj.rolName
        rol_obj = TRol.query.filter_by(rolName=rol_name).first()

        print("HEMOS PASADO EL PRIMER QUERY")

        if not rol_obj:
            return jsonify({"message": "Rol no encontrado"}), 404
        
        # Verificar permisos para pantalla solicitada
        permiso = TPermiso.query.filter_by(rolName=rol_name, pantalla=pantalla).first()

        if not permiso:
            return jsonify({"message": "Acceso denegado a la pantalla solicitada"}), 403
        #if not permiso.acceso:
        #    return jsonify({"message": "No tiene acceso a esta pantalla"}), 403

        # Si el rol tiene permisos, se continua
        return jsonify({"message": f"Bienvenido, {user}", "acceso": permiso.acceso, "modificacion": permiso.modificacion}), 200
    except Exception as e:
        return jsonify({"message": f"Error en el servidor: {str(e)}"}), 500