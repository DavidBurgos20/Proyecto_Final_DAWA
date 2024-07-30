from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class UserComponent:

    @staticmethod
    def getAllUsers():
        try:
            result = False
            data = None
            message = None
            sql = "SELECT * FROM Usuarios"

            result_user = DataBaseHandle.getRecords(sql, 0)
            if result_user['result']:
                result = True
                data = result_user['data']
            else:
                message = 'Error al Obtener datos de usuarios -> ' + result_user['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def insertUser(nombre, correo, contraseña, foto, fecha_nacimiento, biografia):
        try:
            result = False
            data = None
            message = None
            sql = "INSERT INTO Usuarios (nombre, correo_electronico, contraseña, foto_perfil, fecha_nacimiento, biografia) VALUES (%s, %s, %s, %s, %s, %s)"
            record = (nombre, correo, contraseña, foto, fecha_nacimiento, biografia)

            result_insert = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_insert['result']:
                result = True
                data = result_insert['data']
                message = 'Usuario Insertado con Éxito'
            else:
                message = 'Error al Insertar Usuario -> ' + result_insert['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def updateUser(user_id, nombre, correo, contraseña, foto, fecha_nacimiento, biografia):
        try:
            result = False
            data = None
            message = None
            sql = """
            UPDATE Usuarios
            SET nombre = %s, correo_electronico = %s, contraseña = %s, foto_perfil = %s,
                fecha_nacimiento = %s, biografia = %s
            WHERE id = %s
            """
            record = (nombre, correo, contraseña, foto, fecha_nacimiento, biografia, user_id)

            result_update = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_update['result']:
                result = True
                data = result_update['data']
                message = 'Usuario Actualizado con Éxito'
            else:
                message = 'Error al Actualizar Usuario -> ' + result_update['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def deleteUser(user_id):
        try:
            result = False
            data = None
            message = None
            sql = "DELETE FROM Usuarios WHERE id = %s"
            record = (user_id,)

            result_delete = DataBaseHandle.ExecuteNonQuery(sql, record)
            if result_delete['result']:
                result = True
                data = result_delete['data']
                message = 'Usuario Eliminado con Éxito'
            else:
                message = 'Error al Eliminar Usuario -> ' + result_delete['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def getUserDetails(user_id):
        try:
            result = False
            data = None
            message = None
            sql = """
                   SELECT id, nombre, correo_electronico, foto_perfil, fecha_nacimiento, biografia, fecha_creacion 
                   FROM Usuarios 
                   WHERE id = %s
               """
            record = (user_id,)

            result_user = DataBaseHandle.getRecords(sql, 1, record)
            if result_user['result']:
                result = True
                data = result_user['data']
            else:
                message = 'Error al obtener datos del usuario -> ' + result_user['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def getUserPosts(user_id):
        try:
            result = False
            data = None
            message = None
            sql = "SELECT id, usuario_id, contenido, fecha_publicacion FROM Publicaciones WHERE usuario_id = %s"
            record = (user_id,)

            result_posts = DataBaseHandle.getRecords(sql, 0, record)
            if result_posts['result']:
                result = True
                data = result_posts['data']
            else:
                message = 'Error al obtener publicaciones del usuario -> ' + result_posts['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)