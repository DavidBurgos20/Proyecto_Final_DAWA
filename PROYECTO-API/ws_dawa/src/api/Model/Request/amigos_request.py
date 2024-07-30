from marshmallow import Schema, fields

class AmigosRequest(Schema):
    usuario_id_1 = fields.Integer(required=True)
    usuario_id_2 = fields.Integer(required=True)
