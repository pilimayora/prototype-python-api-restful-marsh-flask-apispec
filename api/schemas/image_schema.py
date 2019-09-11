import marshmallow as ma


class ImageSchema(ma.Schema):
    id = ma.fields.Int()
    name = ma.fields.Str()
    width = ma.fields.Int()
