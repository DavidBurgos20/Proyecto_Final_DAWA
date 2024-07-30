from flask import request, jsonify
from flask_restful import Resource
from ..Components.reaction_component import ReactionComponent
from ..Model.Request.reaction_request import ReactionRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found

class ReactionListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de listar reacciones")
            resultado = ReactionComponent.getAllReactions()

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

class ReactionCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de crear reacción")
            rq_json = request.get_json()
            new_reaction = ReactionRequest()
            error_en_validacion = new_reaction.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = ReactionComponent.insertReaction(rq_json['usuario_id'], rq_json['publicacion_id'], rq_json['tipo_reaccion'])
            if resultado['result']:
                return response_success("Reacción creada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class ReactionUpdateService(Resource):
    @staticmethod
    def put(reaction_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de actualizar reacción")
            rq_json = request.get_json()
            new_reaction = ReactionRequest()
            error_en_validacion = new_reaction.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = ReactionComponent.updateReaction(reaction_id, rq_json['tipo_reaccion'])
            if resultado['result']:
                return response_success("Reacción actualizada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class ReactionDeleteService(Resource):
    @staticmethod
    def delete(reaction_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminar reacción")
            resultado = ReactionComponent.deleteReaction(reaction_id)
            if resultado['result']:
                return response_success("Reacción eliminada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
