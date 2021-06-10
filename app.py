# import os module, env variables, Flask modules needed.
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# create instance of Flask 
app = Flask(__name__)

# additional configuration 
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")# grabs DB name
app.config["MONGO_URI"] = os.environ.get("MONGO_URI") # connection string
app.secret_key = os.environ.get("SECRET_KEY") # required for flask security functionality

# create instance of pymongo and pass it the flask app
mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"inputEmail": request.form.get("inputEmail").lower()})
        
        if existing_user:
            flash("User already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("inputEmail").lower(),
            "password": generate_password_hash(
                request.form.get("inputPassword")),
            "firstName": request.form.get("inputFirstName").lower(),
            "lastName": request.form.get("inputLastName").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("inputEmail")
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


# tell the app where and when to run the app. IP & PORT Vars hidden in env.py
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)