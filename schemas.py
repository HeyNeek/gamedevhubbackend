from marshmallow import Schema, fields

class DevSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)