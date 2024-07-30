from flask import request
from flask_restful import Resource

from ..Components.login_component import LoginComponent
from ..Model.Request.login_request import LoginRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success


class LoginService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Login")
            # Obtener el request
            rq_json = request.get_json()
            # Validar ese request sea compatible con el modelo
            new_request = LoginRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = LoginComponent.login(rq_json['login_email'], rq_json['login_password'])
            if resultado['result']:
                return response_success("Login Exitoso")
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class UserService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Executing user ID retrieval service")
            email = request.args.get('email')
            if not email:
                return response_error("Email parameter is required")

            result = LoginComponent.get_user_id(email)
            if result['result']:
                return response_success(result['data'])
            else:
                return response_error(result['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error in method: " + err.__str__())

