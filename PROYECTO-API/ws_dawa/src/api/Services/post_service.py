from flask import request
from flask import request, jsonify
from flask_restful import Resource
from ..Components.post_component import PostComponent
from ..Model.Request.post_request import PostRequest
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found

class PostListService(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de listar publicaciones")
            resultado = PostComponent.getAllPosts()

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

class PostCreateService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de crear publicación")
            rq_json = request.get_json()
            new_request = PostRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = PostComponent.insertPost(rq_json['usuario_id'], rq_json['contenido'])
            if resultado['result']:
                return response_success("Publicación creada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class PostUpdateService(Resource):
    @staticmethod
    def put(post_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de actualizar publicación")
            rq_json = request.get_json()
            new_request = PostRequest()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                HandleLogs.write_error("Error al validar el request -> " + str(error_en_validacion))
                return response_error("Error al validar el request -> " + str(error_en_validacion))

            resultado = PostComponent.updatePost(post_id, rq_json['contenido'])
            if resultado['result']:
                return response_success("Publicación actualizada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class PostDeleteService(Resource):
    @staticmethod
    def delete(post_id):
        try:
            HandleLogs.write_log("Ejecutando servicio de eliminar publicación")
            resultado = PostComponent.deletePost(post_id)
            if resultado['result']:
                return response_success("Publicación eliminada con éxito")
            else:
                return response_error(resultado['message'])
        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
