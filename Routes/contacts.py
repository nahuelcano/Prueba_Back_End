from flask import Blueprint, render_template, request, flash
from requests import request
###  from Models.Tables import Estado, Municipio, Colonia ### IMPOTES DE FORMS
from Utils.db import db


contacts = Blueprint("contacts", __name__)


@contacts.route(
    "/",
)
def index():
    return render_template("index.html")


@contacts.route("/estados")
def estados():

    return render_template("estados.html")


@contacts.route("/municipios")
def municipios():
    return render_template("municipios.html")


@contacts.route("/colonias")
def colonias():
    return render_template("colonias.html")


@contacts.route("/about")
def about():
    return render_template("about.html")
