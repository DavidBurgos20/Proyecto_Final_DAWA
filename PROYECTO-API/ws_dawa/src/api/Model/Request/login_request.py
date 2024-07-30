from marshmallow import Schema, fields


class LoginRequest(Schema):
    login_email = fields.String(required=True)
    login_password = fields.String(required=True)


