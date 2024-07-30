from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class LoginComponent:

    @staticmethod
    def login(p_email, p_password):
        try:
            result = False
            data = None
            message = None
            sql = "SELECT count(*) as valor FROM Usuarios WHERE correo_electronico = %s AND contraseña = %s"
            record = (p_email, p_password)

            resul_login = DataBaseHandle.getRecords(sql, 1, record)
            if resul_login['result']:
                if resul_login['data']['valor'] > 0:
                    result = True
                    message = 'Login Exitoso'
                else:
                    message = 'Login No Válido'
            else:
                message = resul_login['message']

        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def get_user_id(email):
        try:
            result = False
            data = None
            message = None
            sql = "SELECT id FROM Usuarios WHERE correo_electronico = %s"
            record = (email,)

            resul_user = DataBaseHandle.getRecords(sql, 1, record)
            HandleLogs.write_log(
                f"Resultado de la consulta: {resul_user}")  # Log para inspeccionar el resultado de la consulta
            if resul_user['result']:
                if resul_user['data']:
                    result = True
                    # Se asume que resul_user['data'] es un diccionario en lugar de una lista de diccionarios
                    data = {
                        'id': resul_user['data']['id']
                    }
                    message = 'User ID retrieved successfully'
                else:
                    message = 'User not found'
                    HandleLogs.write_log(
                        f"No se encontraron datos para el email: {email}")  # Log de advertencia cuando no se encuentran datos
            else:
                message = resul_user['message']
                HandleLogs.write_error(f"Error en la consulta SQL: {message}")  # Log de error en la consulta SQL

        except KeyError as key_err:
            HandleLogs.write_error(f"KeyError en get_user_id: {key_err}")  # Log de la excepción KeyError
            message = f"KeyError: {key_err}"
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
            HandleLogs.write_error(f"Excepción en get_user_id: {message}")  # Log de la excepción
        finally:
            return internal_response(result, data, message)
