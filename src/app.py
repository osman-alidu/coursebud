from db import *
from table_init import *
import json
from flask import Flask, request
import os


app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()
    course_init()


def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


def str_lst_sum(lst):
    sum = 0
    for x in lst:
        sum += int(x)
    return sum


def l_avg(lst):
    print("-------------------------------------------------------------------")
    print(lst)
    return str_lst_sum(lst)/len(lst)


@app.route("/")
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
        return failure_response("Course not found!")
    body = json.loads(request.data)
    n_rating = body.get('rating')
    if n_rating > 10 or n_rating < 0:
        return failure_response("Invalid rating!")
    rating_str = course.allratings + "," + str(n_rating)
    print("***********************************************")
    print(rating_str)
    rating_lst = rating_str.split(",")
    course.code = body.get('code', course.code)
    course.name = body.get('name', course.name)
    course.description = body.get('description', course.description)
    course.professors = body.get('professors', course.professors)
    course.rating = l_avg(rating_lst)
    course.allratings = course.allratings + "," + str(n_rating)
    course.comments = body.get('comments', course.comments)
    db.session.commit()
    return success_response(course.serialize(), 201)


@app.route("/api/courses/<int:course_id>/", methods=["DELETE"])
def del_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("Course not found!", 404)
    db.session.delete(course)
    db.session.commit()
    return json.dumps(course.serialize()), 200


@app.route("/api/courses/<int:ncourse_id>/comments/")
def get_course_comments(ncourse_id):
    course = Course.query.filter_by(id=ncourse_id).first()
    if course is None:
        return failure_response("Course comments not found!", 404)
    com_list = [t.serialize()
                for t in Comment.query.filter_by(course_id=ncourse_id)]
    db.session.commit()
    return json.dumps({"comments": com_list}), 200


@app.route("/api/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    name = body.get('name')
    email = body.get('email')
    if name == None or email == None:
        return failure_response("Invalid User", 400)
    new_user = User(
        name=body.get('name'),
        email=body.get('email'),
        comments=[]
    )
    db.session.add(new_user)
    db.session.commit()
    return json.dumps(new_user.serialize()), 201


@app.route('/api/users/<int:user_id>/')
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!", 404)
    return json.dumps(user.serialize()), 200


@app.route("/api/users/<int:user_id>/", methods=["POST"])
def update_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response('User not found!')
    body = json.loads(request.data)
    user.name = body.get('name', user.name)
    user.email = body.get('email', user.email)
    user.comments = body.get('comments', user.comments)
    db.session.commit()
    return success_response(user.serialize(), 201)


@app.route("/api/users/<int:user_id>/", methods=["DELETE"])
def del_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!")
    db.session.delete(user)
    db.session.commit()
    return success_response(user.serialize())


@app.route("/api/users/<int:nuser_id>/comments/")
def get_user_comments(nuser_id):
    user = User.query.filter_by(id=nuser_id).first()
    if user is None:
        return failure_response("user not found!", 404)
    com_list = [t.serialize()
                for t in Comment.query.filter_by(user_id=nuser_id)]
    db.session.commit()
    return json.dumps({"comments": com_list}), 200


@app.route("/api/users/<int:user_id>/<int:course_id>/comments/", methods=["POST"])
def add_comment(user_id, course_id):
    body = json.loads(request.data)
    text = body.get('text')
    if text is None:
        return failure_response("Invalid comment", 400)
    new_comment = Comment(
        text=body.get('text'),
        course_id=course_id,
        user_id=user_id
    )
    db.session.add(new_comment)
    db.session.commit()
    return json.dumps(new_comment.serialize()), 201


@app.route('/api/comments/<int:comment_id>/')
def get_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if comment is None:
        return failure_response("comment not found!", 404)
    return json.dumps(comment.serialize()), 200


@app.route("/api/comments/<int:comment_id>/", methods=["DELETE"])
def del_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if comment is None:
        return failure_response("Comment not found!")
    db.session.delete(comment)
    db.session.commit()
    return success_response(comment.serialize())


# def extract_token(request):
#     pass


# @app.route("/register/", methods=["POST"])
# def register_account():
#     pass


# @app.route("/login/", methods=["POST"])
# def login():
#     pass


# @app.route("/session/", methods=["POST"])
# def update_session():
#     pass


# @app.route("/secret/", methods=["GET"])
# def secret_message():
#     pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
