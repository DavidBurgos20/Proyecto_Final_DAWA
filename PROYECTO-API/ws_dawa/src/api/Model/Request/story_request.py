from marshmallow import Schema, fields

class StoryRequest(Schema):
    usuario_id = fields.Integer(required=True)
    contenido = fields.String(required=True)
