from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class ReactionComponent:

    @staticmethod
    def getAllReactions():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Reacciones"

            result_reactions = DataBaseHandle.getRecords(sql, 0)
            if result_reactions['result']:
                result = True
                data = result_reactions['data']
            else:
                message = 'Error al obtener datos de reacciones -> ' + result_reactions['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertReaction(usuario_id, publicacion_id, tipo_reaccion):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Reacciones (usuario_id, publicacion_id, tipo_reaccion) VALUES (%s, %s, %s)"
            record = (usuario_id, publicacion_id, tipo_reaccion)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Reacción insertada con éxito'
            else:
                message = 'Error al insertar reacción -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updateReaction(reaction_id, tipo_reaccion):
        try:
            result = False
            data = None
            message = None
            sql = "UPDATE Reacciones SET tipo_reaccion = %s WHERE id = %s"
            record = (tipo_reaccion, reaction_id)

            result_update = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_update['result']:
                result = True
                data = result_update['data']
                message = 'Reacción actualizada con éxito'
            else:
                message = 'Error al actualizar reacción -> ' + result_update['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deleteReaction(reaction_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Reacciones WHERE id = %s"
            record = (reaction_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Reacción eliminada con éxito'
            else:
                message = 'Error al eliminar reacción -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
