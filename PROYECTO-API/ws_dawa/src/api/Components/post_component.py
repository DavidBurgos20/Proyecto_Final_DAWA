from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class PostComponent:

    @staticmethod
    def getAllPosts():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Publicaciones"

            result_posts = DataBaseHandle.getRecords(sql, 0)
            if result_posts['result']:
                result = True
                data = result_posts['data']
            else:
                message = 'Error al obtener datos de publicaciones -> ' + result_posts['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertPost(usuario_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Publicaciones (usuario_id, contenido) VALUES (%s, %s)"
            record = (usuario_id, contenido)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Publicación insertada con éxito'
            else:
                message = 'Error al insertar publicación -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updatePost(post_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "UPDATE Publicaciones SET contenido = %s WHERE id = %s"
            record = (contenido, post_id)

            result_update = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_update['result']:
                result = True
                data = result_update['data']
                message = 'Publicación actualizada con éxito'
            else:
                message = 'Error al actualizar publicación -> ' + result_update['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deletePost(post_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Publicaciones WHERE id = %s"
            record = (post_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Publicación eliminada con éxito'
            else:
                message = 'Error al eliminar publicación -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
