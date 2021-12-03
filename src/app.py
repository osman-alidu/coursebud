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


def extract_token(request):
    token = request.headers.get("Authorization")
    if token is None:
        return False, "Missing Authorization header"
    token = token.replace("Bearer", "").strip()
    return True, token


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


@app.route("/")
def hello_world():
    return json.dumps({"message": "Hello, World!"})


@app.route("/api/users/register/", methods=["POST"])
def register_account():
    body = json.loads(request.data)
    username = body.get('username')
    email = body.get('email')
    password = body.get('password')
    if email is None or password is None or username is None:
        return failure_response("Invalid username, email or password!", 400)

    created, user = create_r_user(username, email, password)

    if not created:
        return failure_response("User already exists!", 403)

    return success_response({
        "user_id": user.id,
        "session_token": user.session_token,
        "session_expiration": str(user.session_expiration),
        "update_token": user.update_token
    })


@app.route("/api/users/login/", methods=["POST"])
def login():
    body = json.loads(request.data)
    username = body.get('username')
    email = body.get('email')
    password = body.get('password')
    if email is None or password is None or username is None:
        return failure_response("Invalid username, email or password!", 400)

    valid_cred, user = verify_creds(username, email, password)

    if not valid_cred:
        return failure_response("wrong password!", 403)

    return success_response({
        "user_id": user.id,
        "session_token": user.session_token,
        "session_expiration": str(user.session_expiration),
        "update_token": user.update_token
    })


@app.route("/api/users/session/", methods=["POST"])
def update_session():
    success, update_token = extract_token(request)

    if not success:
        return failure_response(update_token)

    valid, user = renew_session_l(update_token)

    if not valid:
        return failure_response("Invalid update token", 403)

    return success_response({
        "user_id": user.id,
        "session_token": user.session_token,
        "session_expiration": str(user.session_expiration),
        "update_token": user.update_token
    })


@app.route("/api/users/secret/", methods=["GET"])
def secret_message():
    success, session_token = extract_token(request)

    if not success:
        return failure_response(session_token)

    valid = verify_session(session_token)

    if not valid:
        return failure_response("Invalid session token", 403)

    return success_response("Hello World!")


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
    rating_lst = rating_str.split(",")
    course.code = body.get('code', course.code)
    course.name = body.get('name', course.name)
    course.description = body.get('description', course.description)
    course.professors = body.get('professors', course.professors)
    course.rating = avg(rating_lst)
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
    user.username = body.get('username', user.username)
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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
