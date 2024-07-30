from flask import request
from flask import request, jsonify
from flask_restful import Resource
from ..Components.story_component import StoryComponent
from ..Model.Request.story_request import StoryRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found

class StoryListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de listar historias")
            resultado = StoryComponent.getAllStories()

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

class StoryCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de crear historia")
            rq_json = request.get_json()
            new_request = StoryRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = StoryComponent.insertStory(rq_json['usuario_id'], rq_json['contenido'])
            if resultado['result']:
                return response_success("Historia creada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class StoryUpdateService(Resource):
    @staticmethod
    def put(story_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de actualizar historia")
            rq_json = request.get_json()
            new_request = StoryRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = StoryComponent.updateStory(story_id, rq_json['contenido'])
            if resultado['result']:
                return response_success("Historia actualizada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class StoryDeleteService(Resource):
    @staticmethod
    def delete(story_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminar historia")
            resultado = StoryComponent.deleteStory(story_id)
            if resultado['result']:
                return response_success("Historia eliminada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
