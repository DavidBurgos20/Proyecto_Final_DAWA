from flask import request, jsonify
from flask_restful import Resource
from ..Components.message_component import MessageComponent
from ..Model.Request.message_request import MessageRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found

class MessageListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de listar mensajes")
            resultado = MessageComponent.getAllMessages()

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

class MessageDetailService(Resource):
    @staticmethod
    def get(remitente_id, destinatario_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de obtener mensajes por remitente y destinatario")
            resultado = MessageComponent.getMessagesBySenderAndRecipient(remitente_id, destinatario_id)

            if resultado['result']:
                if resultado['data']:
                    return jsonify(response_success(resultado['data']))
                else:
                    return jsonify(response_not_found())
            else:
                return jsonify(response_error(resultado['message']))
        except Exception as err:
            HandleLogs.write_error(err)
            return jsonify(response_error("Error en el método: " + str(err)))

class MessageCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de crear mensaje")
            rq_json = request.get_json()
            new_message = MessageRequest()
            error_en_validacion = new_message.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = MessageComponent.insertMessage(rq_json['remitente_id'], rq_json['destinatario_id'], rq_json['contenido'])
            if resultado['result']:
                return response_success("Mensaje creado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class MessageUpdateService(Resource):
    @staticmethod
    def put(message_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de actualizar mensaje")
            rq_json = request.get_json()
            new_message = MessageRequest()
            error_en_validacion = new_message.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = MessageComponent.updateMessage(message_id, rq_json['contenido'])
            if resultado['result']:
                return response_success("Mensaje actualizado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class MessageDeleteService(Resource):
    @staticmethod
    def delete(message_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminar mensaje")
            resultado = MessageComponent.deleteMessage(message_id)
            if resultado['result']:
                return response_success("Mensaje eliminado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
