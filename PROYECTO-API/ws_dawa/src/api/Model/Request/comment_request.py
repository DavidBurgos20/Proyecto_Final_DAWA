from marshmallow import Schema, fields

class CommentRequest(Schema):
    usuario_id = fields.Integer(required=True)
    post_id = fields.Integer(required=True)
    contenido = fields.String(required=True)
