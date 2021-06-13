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
            {"email": request.form.get("inputEmail").lower()})
        
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
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("inputPassword")):
                    session["user"] = request.form.get("inputEmail").lower()
                    # flash("Welcome {}!".format(
                    #     existing_user['firstName'].title()))
                    return redirect(
                        url_for("profile", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    tasks = list(mongo.db.tasks.find())
    username = mongo.db.users.find_one(
        {"email": session["user"]})['firstName'].title()

    if session["user"]:
        return render_template("profile.html", username=username, tasks=tasks)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))



# tell the app where and when to run the app. IP & PORT Vars hidden in env.py
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)