from flask import request
from flask_restful import Resource
from flask import jsonify
from datetime import date
from ..Components.user_component import UserComponent
from ..Model.Request.user_request import UserRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found


class UserListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar Usuario")
            resultado = UserComponent.getAllUsers()

            # Convertir fechas a cadenas de texto
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    for user in resultado['data']:
                        if isinstance(user.get('fecha_nacimiento'), date):
                            user['fecha_nacimiento'] = user['fecha_nacimiento'].isoformat()
                    return jsonify(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())


class UserCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear Usuario")
            rq_json = request.get_json()
            new_request = UserRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = UserComponent.insertUser(
                rq_json['nombre'], rq_json['correo_electronico'], rq_json['contraseña'],
                rq_json.get('foto_perfil'), rq_json.get('fecha_nacimiento'), rq_json.get('biografia')
            )
            if resultado['result']:
                return response_success("Usuario Creado con Éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())


class UserUpdateService(Resource):
    @staticmethod
    def put(user_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de Actualizar Usuario")
            rq_json = request.get_json()
            new_request = UserRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = UserComponent.updateUser(
                user_id, rq_json['nombre'], rq_json['correo_electronico'], rq_json['contraseña'],
                rq_json.get('foto_perfil'), rq_json.get('fecha_nacimiento'), rq_json.get('biografia')
            )
            if resultado['result']:
                return response_success("Usuario Actualizado con Éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())


class UserDeleteService(Resource):
    @staticmethod
    def delete(user_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Usuario")
            resultado = UserComponent.deleteUser(user_id)
            if resultado['result']:
                return response_success("Usuario Eliminado con Éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class UserDetailsService(Resource):
    @staticmethod
    def get(user_id):
        try:
            HandleLogs.write_log(f"Ejecutando servicio de obtener detalles del usuario: {user_id}")
            resultado = UserComponent.getUserDetails(user_id)
            if resultado['result']:
                return jsonify(resultado['data'])
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class UserPostsService(Resource):
    @staticmethod
    def get(user_id):
        try:
            HandleLogs.write_log(f"Ejecutando servicio de obtener publicaciones del usuario: {user_id}")
            resultado = UserComponent.getUserPosts(user_id)
            if resultado['result']:
                return jsonify(resultado['data'])
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())