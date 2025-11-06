import fields as fields
import flask
from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sampleDatabase.db'
db = SQLAlchemy(app)

class VideoDB(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer(), nullable=False)
    views = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Video [{self.id}, {self.name}, {self.likes}, {self.views}]'


add_video_args = reqparse.RequestParser()
add_video_args.add_argument("name", type=str, help="Name of the video", required=True)
add_video_args.add_argument("views", type=int, help="Number of views on the video", required=True)
add_video_args.add_argument("likes", type=int, help="Number of likes on the video", required=True)

videos = {}

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "likes": fields.Integer,
    "views": fields.Integer,
}
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        res = VideoDB.query.filter_by(id=video_id).first()
        return res

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = add_video_args.parse_args()
        res = VideoDB.query.filter_by(id=video_id).first()
        if res:
            abort(409, "Video is already taken......")
        video = VideoDB(id=video_id, name=args['name'], likes=args['likes'], views=args['views'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def delete(self, video_id):
        video = VideoDB.query.filter_by(id=video_id).first()
        if not video: abort(404, message="Requested Video is not found....")
        db.session.delete(video)
        db.session.commit()
        return "Deleted successfully...", 404

api.add_resource(Video, '/video/<int:video_id>')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
