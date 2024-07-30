
from flask import request, jsonify
from flask_restful import Resource
from ..Components.amigos_component import AmigosComponent
from ..Model.Request.amigos_request import AmigosRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found

class AmigosListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de listar amigos")
            resultado = AmigosComponent.getAllAmigos()

            if resultado['result']:
                if len(resultado['data']) > 0:
                    return jsonify(response_success(resultado['data']))
                else:
                    return jsonify(response_not_found())
            else:
                return jsonify(response_error(resultado['message']))
        except Exception as err:
            HandleLogs.write_error(err)
            return jsonify(response_error("Error en el método: " + str(err)))

class AmigosCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de crear amigo")
            rq_json = request.get_json()
            new_request = AmigosRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = AmigosComponent.insertAmigo(rq_json['usuario_id_1'], rq_json['usuario_id_2'])
            if resultado['result']:
                return response_success("Amigo creado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class AmigosDeleteService(Resource):
    @staticmethod
    def delete(amigo_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminar amigo")
            resultado = AmigosComponent.deleteAmigo(amigo_id)
            if resultado['result']:
                return response_success("Amigo eliminado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
