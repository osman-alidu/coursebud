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


def str_lst_sum(lst):
    sum = 0
    for x in lst:
        sum += int(x)
    return sum


def avg(lst):
    return str_lst_sum(lst)/len(lst)

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
        allratings="0",
        comments=[]
    )
    db.session.add(new_course)
    db.session.commit()
    return json.dumps(new_course.serialize()), 201


@app.route("/api/courses/<int:course_id>/")
def get_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("Course not found!", 404)
    return json.dumps(course.serialize()), 200


@app.route("/api/courses/<int:course_id>/", methods=["POST"])
def update_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("course not found!")
    body = json.loads(request.data)
    n_rating = body.get('rating')
    rating_lst = list(course.allratings + str(n_rating))
    course.code = body.get('code', course.code)
    course.name = body.get('name', course.name)
    course.description = body.get('description', course.description)
    course.professors = body.get('professors', course.professors)
    course.rating = avg(rating_lst)
    course.allratings = course.allratings + str(n_rating)
    course.comments = body.get('comments', course.comments)
    db.session.commit()
    return success_response(course.serialize(), 201)


@app.route("/api/courses/<int:course_id>/", methods=["DELETE"])
def del_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("course not found!", 404)
    db.session.delete(course)
    db.session.commit()
    return json.dumps(course.serialize()), 200


@app.route("/api/courses/<int:ncourse_id>/comments/")
def get_course_comments(ncourse_id):
    course = Course.query.filter_by(id=ncourse_id).first()
    if course is None:
        return failure_response("course not found!", 404)
    com_list = [t.serialize()
                for t in Comment.query.filter_by(course_id=ncourse_id)]
    db.session.commit()
    return json.dumps({"comments": com_list}), 200


@app.route("/api/users/", methods=["POST"])
def create_user():
    pass


@app.route("/api/users/<int:user_id>/")
def update_user():
    pass


@app.route("/api/users/<int:nuser_id>/comments/")
def get_user_comments(nuser_id):
    user = User.query.filter_by(id=nuser_id).first()
    if user is None:
        return failure_response("user not found!", 404)
    com_list = [t.serialize()
                for t in Comment.query.filter_by(user_id=nuser_id)]
    db.session.commit()
    return json.dumps({"comments": com_list}), 200


@app.route("/api/users/<int:user_id>/")
def del_user():
    pass


@app.route("/api/users/<int:user_id>/comments/", methods=["POST"])
def add_comment():
    pass


@app.route("/api/comments/", methods=["POST"])
def del_comment():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
