from flask_apispec import doc, marshal_with, use_kwargs, MethodResource

from marshmallow import fields
from api.models.image import Image
from api.schemas.image_schema import ImageSchema


@doc(tags=['images'])
class ImageResource(MethodResource):

    @doc(description="Returns an image by id")
    @use_kwargs({'id': fields.Int(required=True)}, locations=["query"])
    @marshal_with(ImageSchema, code=200)
    def get(self, **kwargs):
        return Image('test', 1000)

    @use_kwargs(ImageSchema)
    @marshal_with(ImageSchema, code=201)
    def post(self):
        return Image('test', 500)


@doc(tags=['images'])
class ImageListResource(MethodResource):

    @doc(description="Returns all images")
    @marshal_with(ImageSchema(many=True), code=200)
    def get(self):
        return [Image('test', 1000)]
