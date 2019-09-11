import flask
from flask_restful import Api

from flask_apispec import FlaskApiSpec

from api.endpoints.images import ImageResource, ImageListResource
from api.endpoints.videos import VideoResource, VideoListResource


app = flask.Flask(__name__)
api = Api(app)

api.add_resource(ImageResource, '/image/')
api.add_resource(ImageListResource, '/images/')
api.add_resource(VideoResource, '/video/')
api.add_resource(VideoListResource, '/videos/')

app.config['APISPEC_TITLE'] = "Flask-apispec DataVault Prototype"
docs = FlaskApiSpec(app)

app.add_url_rule('/image/', view_func=ImageResource.as_view('Image'))
docs.register(ImageResource)
app.add_url_rule('/images/', view_func=ImageListResource.as_view('Images'))
docs.register(ImageListResource)
app.add_url_rule('/video/', view_func=VideoResource.as_view('Video'))
docs.register(VideoResource)
app.add_url_rule('/videos/', view_func=VideoListResource.as_view('Videos'))
docs.register(VideoListResource)


if __name__ == '__main__':
    app.run(debug=True)
