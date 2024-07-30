from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class CommentComponent:

    @staticmethod
    def getAllComments():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Comentarios"

            result_comments = DataBaseHandle.getRecords(sql, 0)
            if result_comments['result']:
                result = True
                data = result_comments['data']
            else:
                message = 'Error al obtener datos de comentarios -> ' + result_comments['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertComment(usuario_id, post_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Comentarios (usuario_id, post_id, contenido) VALUES (%s, %s, %s)"
            record = (usuario_id, post_id, contenido)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Comentario insertado con éxito'
            else:
                message = 'Error al insertar comentario -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updateComment(comment_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "UPDATE Comentarios SET contenido = %s WHERE id = %s"
            record = (contenido, comment_id)

            result_update = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_update['result']:
                result = True
                data = result_update['data']
                message = 'Comentario actualizado con éxito'
            else:
                message = 'Error al actualizar comentario -> ' + result_update['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deleteComment(comment_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Comentarios WHERE id = %s"
            record = (comment_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Comentario eliminado con éxito'
            else:
                message = 'Error al eliminar comentario -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
