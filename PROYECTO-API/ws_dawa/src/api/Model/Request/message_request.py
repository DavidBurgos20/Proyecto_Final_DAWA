from marshmallow import Schema, fields

class MessageRequest(Schema):
    remitente_id = fields.Integer(required=True)
    destinatario_id = fields.Integer(required=True)
    contenido = fields.String(required=True)
