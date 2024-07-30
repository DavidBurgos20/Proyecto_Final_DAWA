from flask import request, jsonify
from flask_restful import Resource
from ..Components.comment_component import CommentComponent
from ..Model.Request.comment_request import CommentRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found

class CommentListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de listar comentarios")
            resultado = CommentComponent.getAllComments()

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


class CommentCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de crear comentario")
            rq_json = request.get_json()
            new_comment = CommentRequest()
            error_en_validacion = new_comment.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = CommentComponent.insertComment(rq_json['usuario_id'], rq_json['post_id'], rq_json['contenido'])
            if resultado['result']:
                return response_success("Comentario creado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class CommentUpdateService(Resource):
    @staticmethod
    def put(comment_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de actualizar comentario")
            rq_json = request.get_json()
            new_comment = CommentRequest()
            error_en_validacion = new_comment.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = CommentComponent.updateComment(comment_id, rq_json['contenido'])
            if resultado['result']:
                return response_success("Comentario actualizado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class CommentDeleteService(Resource):
    @staticmethod
    def delete(comment_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminar comentario")
            resultado = CommentComponent.deleteComment(comment_id)
            if resultado['result']:
                return response_success("Comentario eliminado con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
