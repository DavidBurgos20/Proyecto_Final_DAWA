from marshmallow import Schema, fields

class ReactionRequest(Schema):
    usuario_id = fields.Integer(required=True)
    publicacion_id = fields.Integer(required=True)
    tipo_reaccion = fields.String(required=True)
