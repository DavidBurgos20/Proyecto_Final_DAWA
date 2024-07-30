from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class FriendRequestComponent:

    @staticmethod
    def getAllFriendRequests():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Solicitudes_Amistad"

            result_requests = DataBaseHandle.getRecords(sql, 0)
            if result_requests['result']:
                result = True
                data = result_requests['data']
            else:
                message = 'Error al obtener datos de solicitudes de amistad -> ' + result_requests['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertFriendRequest(remitente_id, destinatario_id, estado):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Solicitudes_Amistad (remitente_id, destinatario_id, estado) VALUES (%s, %s, %s)"
            record = (remitente_id, destinatario_id, estado)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Solicitud de amistad insertada con éxito'
            else:
                message = 'Error al insertar solicitud de amistad -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updateFriendRequest(request_id, estado):
        try:
            result = False
            data = None
            message = None
            sql = "UPDATE Solicitudes_Amistad SET estado = %s WHERE id = %s"
            record = (estado, request_id)

            result_update = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_update['result']:
                result = True
                data = result_update['data']
                message = 'Solicitud de amistad actualizada con éxito'
            else:
                message = 'Error al actualizar solicitud de amistad -> ' + result_update['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deleteFriendRequest(request_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Solicitudes_Amistad WHERE id = %s"
            record = (request_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Solicitud de amistad eliminada con éxito'
            else:
                message = 'Error al eliminar solicitud de amistad -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
