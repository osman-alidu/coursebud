from flask_sqlalchemy import SQLAlchemy
# import bcrypt

import datetime
import hashlib
import os

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
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    comments = db.relationship("Comment", cascade="delete")

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "comments": [s.simple_serialize() for s in self.comments],
        }

    def simple_serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
