import os

from flask import Blueprint
from flask import __version__
from flask import render_template, jsonify, request

from hello.models.User import User
from config.settings import DEBUG
from hello.extensions import db

page = Blueprint("page", __name__, template_folder="templates")


@page.get("/")
def home():
    return render_template(
        "page/home.html",
        flask_ver=__version__,
        python_ver=os.environ["PYTHON_VERSION"],
        debug=DEBUG,
    )


@page.get("/api/user")
def api_get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])


@page.get("/api/user/<int:id>")
def api_get_user(id):
    user = User.query.filter_by(id=id).first()
    return jsonify(user.serialize())


@page.post("/api/user")
def api_post_user():
    user = User(**request.get_json())
    db.session.add(user)
    db.session.commit()
    return jsonify({"status": "success", "id": user.id})
