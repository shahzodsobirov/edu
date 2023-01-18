from app import *
from flask_migrate import Migrate
from sqlalchemy import String, Integer, Column
from flask_sqlalchemy import *

db = SQLAlchemy()


def db_setup(app):
    app.config.from_object('backend.config')
    db.app = app
    db.init_app(app)
    Migrate(app, db)
    return db


class School(db.Model):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Student(db.Model):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(String)
    attendance = Column(String)
    score = Column(String)
