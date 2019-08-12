import random

from flask import Blueprint, render_template

from app.ext import db
from app.models import Person #迁移前必须调用下，不然迁移不了

blue = Blueprint("first_blue",__name__)

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route("/")
def index():
    return "hello flask"

@blue.route('/addperson')
def add_person():
    person = Person()
    flag = random.randrange(100)
    person.p_name = "你好小明%d"%flag
    person.p_age = flag
    db.session.add(person)
    db.session.commit()
    return "add success"

@blue.route('/getpersons')
def get_persons():
    persons = Person.query.all()
    return  render_template("personlist.html",persons=persons)