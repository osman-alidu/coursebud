from db import *
import json
from flask import Flask, request


app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


# your routes here

@ app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/api/courses/")
def get_courses():
    courses = [t.serialize() for t in Course.query.all()]
    return json.dumps({"courses": courses}), 200


@app.route("/api/courses/", methods=["POST"])
def create_course():
    body = json.loads(request.data)
    if body.get('code') == None or body.get('name') == None:
        return failure_response("Invalid data", 400)
    new_course = Course(
        code=body.get('code'),
        name=body.get('name'),
        description=body.get('description'),
        professors=body.get('professors'),
        rating=0,
        comments=[]
    )
    db.session.add(new_course)
    db.session.commit()
    return json.dumps(new_course.serialize()), 201


@app.route("/api/courses/<int:course_id>/")
def get_course(course_id):
    pass


@app.route("/api/courses/<int:course_id>/")
def update_course():
    pass


@app.route("/api/courses/<int:course_id>/", methods=["DELETE"])
def del_course():
    pass


@app.route("/api/courses/<int:course_id>/comments")
def get_course_comments():
    pass


@app.route("/api/users/", methods=["POST"])
def create_user():
    pass


@app.route("/api/users/<int:user_id>/")
def update_user():
    pass


@app.route("/api/users/<int:user_id>/comments")
def get_user_comments():
    pass


@app.route("/api/users/<int:user_id>/")
def del_user():
    pass


@app.route("/api/users/<int:user_id>/comments", methods=["POST"])
def add_comment():
    pass


@app.route("/api/comments/", methods=["POST"])
def del_comment():
    pass


@app.route("/api/courses/<int:course_id>/rating", methods=["POST"])
def add_rating():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
