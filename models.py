#  Created by KAR:
#
#  Kyle Awah     - (816012635)
#  Avita John    - (816012533)
#  Riandra Maraj - (816010975)
#  Kyle Sukhdeo  - (816014143)
#
#  AFTR_MARKT
#  (Group Project - Storefront)
#  INFO 2602 - Web Programming and Technologies 1
#
#  models.py contains:
#  - SQLAlchemy Models for the Database

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class user(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    shipping_address = db.Column(db.String(120), nullable=True)
    payment_method = db.Column(db.String(120), nullable=True)
    payment_method_card_number = db.Column(db.Integer, nullable=True)
    login_counter = db.Column(db.Integer, nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "shipping_address": self.shipping_address,
            "payment_method": self.payment_method,
						"login_counter": self.login_counter
        }

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class product_tee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    size = db.Column(db.String(120), nullable=False)
    color = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    catagory = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
						"brand":self.brand,
            "size": self.size,
            "color": self.color,
            "desc": self.desc,
						"catagory": self.catagory
        }


class product_jacket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    size = db.Column(db.String(120), nullable=False)
    color = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    catagory = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
						"brand":self.brand,
            "size": self.size,
            "color": self.color,
            "desc": self.desc,
						"catagory": self.catagory
        }


class product_pants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    size = db.Column(db.String(120), nullable=False)
    color = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    catagory = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
						"brand":self.brand,
            "size": self.size,
            "color": self.color,
            "desc": self.desc,
						"catagory": self.catagory
        }


class product_shoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    catagory = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
						"brand":self.brand,
            "size": self.size,
            "color": self.color,
            "desc": self.desc,
						"catagory": self.catagory
        }


class product_acc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=False)
    color = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    catagory = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
						"brand":self.brand,
            "color": self.color,
            "desc": self.desc,
						"catagory": self.catagory
        }