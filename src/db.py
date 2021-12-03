import datetime
import hashlib
import os

import bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    professors = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    allratings = db.Column(db.String, nullable=False)
    comments = db.relationship("Comment", cascade="delete")

    def __init__(self, **kwargs):
        self.code = kwargs.get("code")
        self.name = kwargs.get("name")
        self.description = kwargs.get("description")
        self.professors = kwargs.get("professors")
        self.rating = kwargs.get("rating")
        self.allratings = kwargs.get("allratings")

    def full_serialize(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "professors": self.professors,
            "rating": self.rating,
            "allratings": self.allratings,
            "comments": [c.simple_serialize() for c in self.comments]
        }

    def serialize(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "professors": self.professors,
            "rating": self.rating,
            "comments": [c.simple_serialize() for c in self.comments]
        }

    def simple_serialize(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "description": self.description,
            "professors": self.professors,
            "rating": self.rating
        }


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey(
        'course.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), nullable=False)

    def __init__(self, **kwargs):
        self.text = kwargs.get("text")
        self.course_id = kwargs.get("course_id")
        self.user_id = kwargs.get("user_id")

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "course": (Course.query.filter_by(id=self.course_id).first()).simple_serialize(),
            "user": (User.query.filter_by(id=self.user_id).first()).simple_serialize()
        }

    def simple_serialize(self):
        return {
            "id": self.id,
            "text": self.text,
        }


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)

    # User information
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_digest = db.Column(db.String, nullable=False)
    comments = db.relationship("Comment", cascade="delete")

    # Session information
    session_token = db.Column(db.String, nullable=False, unique=True)
    session_expiration = db.Column(db.DateTime, nullable=False)
    update_token = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password_digest = bcrypt.hashpw(kwargs.get(
            "password").encode("utf8"), bcrypt.gensalt(rounds=13))
        self.renew_session()

    # Used to randomly generate session/update tokens
    def _urlsafe_base_64(self):
        return hashlib.sha1(os.urandom(64)).hexdigest()

    # Generates new tokens, and resets expiration time
    def renew_session(self):
        self.session_token = self._urlsafe_base_64()
        self.session_expiration = datetime.datetime.now() + datetime.timedelta(days=1)
        self.update_token = self._urlsafe_base_64()

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode("utf8"), self.password_digest)

    # Checks if session token is valid and hasn't expired
    def verify_session_token(self, session_token):
        return session_token == self.session_token and datetime.datetime.now() < self.session_expiration

    def verify_update_token(self, update_token):
        return update_token == self.update_token

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "comments": [s.simple_serialize() for s in self.comments],
        }

    def simple_serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


def create_r_user(username, email, password):
    existing_user = User.query.filter(User.email == email).first()
    if existing_user:
        return False, None
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return True, user


def verify_creds(username, email, password):
    existing_user = User.query.filter(User.email == email).first()
    if not existing_user:
        return False, None

    return existing_user.verify_password(password), existing_user


def renew_session_l(update_token):
    existing_user = User.query.filter(
        User.update_token == update_token).first()
    if not existing_user:
        return False, None

    existing_user.renew_session()
    db.session.commit()
    return True, existing_user


def verify_session(session_token):
    return User.query.filter(
        User.session_token == session_token).first()
