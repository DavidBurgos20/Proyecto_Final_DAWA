from marshmallow import Schema, fields


class UserRequest(Schema):
    nombre = fields.String(required=True)
    correo_electronico = fields.String(required=True)
    contraseña = fields.String(required=True)
    foto_perfil = fields.String(required=False)
    fecha_nacimiento = fields.Date(required=False)
    biografia = fields.String(required=False)
