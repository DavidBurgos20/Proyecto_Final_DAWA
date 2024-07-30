from marshmallow import Schema, fields

class FriendRequestRequest(Schema):
    remitente_id = fields.Integer(required=True)
    destinatario_id = fields.Integer(required=True)
    estado = fields.String(missing="pendiente")
