from flask_apispec import doc, marshal_with, use_kwargs, MethodResource

from marshmallow import fields
from api.models.video import Video
from api.schemas.video_schema import VideoSchema


@doc(tags=['videos'])
class VideoResource(MethodResource):

    @doc(description="Returns a video by id")
    @use_kwargs({'id': fields.Int(required=True)}, locations=["query"])
    @marshal_with(VideoSchema, code=200)
    def get(self, **kwargs):
        return Video('test', 1000)

    @use_kwargs(VideoSchema)
    @marshal_with(VideoSchema(exclude=["id"]), code=201)
    def post(self):
        return Video('test', 500)


@doc(tags=['videos'])
class VideoListResource(MethodResource):

    @doc(description="Returns all videos")
    @marshal_with(VideoSchema(many=True), code=200)
    def get(self):
        return [Video('test', 1000)]
