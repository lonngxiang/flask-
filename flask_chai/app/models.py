from app.ext import db


class Person(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    p_name = db.Column(db.String(18))
    p_age = db.Column(db.Integer,default=18)