from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class StoryComponent:

    @staticmethod
    def getAllStories():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Historias"

            result_stories = DataBaseHandle.getRecords(sql, 0)
            if result_stories['result']:
                result = True
                data = result_stories['data']
            else:
                message = 'Error al obtener datos de historias -> ' + result_stories['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertStory(usuario_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Historias (usuario_id, contenido) VALUES (%s, %s)"
            record = (usuario_id, contenido)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Historia insertada con éxito'
            else:
                message = 'Error al insertar historia -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updateStory(story_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "UPDATE Historias SET contenido = %s WHERE id = %s"
            record = (contenido, story_id)

            result_update = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_update['result']:
                result = True
                data = result_update['data']
                message = 'Historia actualizada con éxito'
            else:
                message = 'Error al actualizar historia -> ' + result_update['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deleteStory(story_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Historias WHERE id = %s"
            record = (story_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Historia eliminada con éxito'
            else:
                message = 'Error al eliminar historia -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
