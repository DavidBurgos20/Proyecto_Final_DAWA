from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class MessageComponent:

    @staticmethod
    def getAllMessages():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Mensajes"

            result_messages = DataBaseHandle.getRecords(sql, 0)
            if result_messages['result']:
                result = True
                data = result_messages['data']
            else:
                message = 'Error al obtener datos de mensajes -> ' + result_messages['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def getMessagesBySenderAndRecipient(remitente_id, destinatario_id):
        try:
            result = False
            data = None
            message = None
            sql = """
            SELECT * FROM Mensajes 
            WHERE (remitente_id = %s AND destinatario_id = %s) 
               OR (remitente_id = %s AND destinatario_id = %s)
            """
            record = (remitente_id, destinatario_id, destinatario_id, remitente_id)

            result_message = DataBaseHandle.getRecords(sql, -1, record)
            if result_message['result']:
                result = True
                data = result_message['data']
            else:
                message = 'Error al obtener los mensajes -> ' + result_message['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertMessage(remitente_id, destinatario_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Mensajes (remitente_id, destinatario_id, contenido) VALUES (%s, %s, %s)"
            record = (remitente_id, destinatario_id, contenido)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Mensaje insertado con éxito'
            else:
                message = 'Error al insertar mensaje -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updateMessage(message_id, contenido):
        try:
            result = False
            data = None
            message = None
            sql = "UPDATE Mensajes SET contenido = %s WHERE id = %s"
            record = (contenido, message_id)

            result_update = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_update['result']:
                result = True
                data = result_update['data']
                message = 'Mensaje actualizado con éxito'
            else:
                message = 'Error al actualizar mensaje -> ' + result_update['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deleteMessage(message_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Mensajes WHERE id = %s"
            record = (message_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Mensaje eliminado con éxito'
            else:
                message = 'Error al eliminar mensaje -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
