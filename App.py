from flask import Flask
from Config import Database
from Routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from Config import Database


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = Database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(contacts)
