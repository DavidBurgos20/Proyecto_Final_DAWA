from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class AmigosComponent:

    @staticmethod
    def getAllAmigos():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Amigos"

            result_amigos = DataBaseHandle.getRecords(sql, 0)
            if result_amigos['result']:
                result = True
                data = result_amigos['data']
            else:
                message = 'Error al obtener datos de amigos -> ' + result_amigos['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertAmigo(usuario_id_1, usuario_id_2):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Amigos (usuario_id_1, usuario_id_2) VALUES (%s, %s)"
            record = (usuario_id_1, usuario_id_2)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Amigo agregado con éxito'
            else:
                message = 'Error al agregar amigo -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deleteAmigo(amigo_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Amigos WHERE id = %s"
            record = (amigo_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Amigo eliminado con éxito'
            else:
                message = 'Error al eliminar amigo -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)
