# import os module, env variables, Flask modules needed.
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField
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
        is_admin = "on" if request.form.get("is_admin") else "off"
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
            "lastName": request.form.get("inputLastName").lower(),
            "is_admin": is_admin,
            "user_name": request.form.get("uname").lower(),
            "address": request.form.get("inputAddress").lower(),
            "city": request.form.get("inputCity").lower(),
            "country": request.form.get("inputCountry").lower(),
            "post_code": request.form.get("postCode").lower()
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("inputEmail")
        #flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/update_profile/<id>", methods=["GET", "POST"])
def update_profile(id):
    if request.method == "POST":
        is_admin = "on" if request.form.get("is_admin") else "off"
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})
        # print(existing_user)

        # record=mongo.db.users.find_one({"email": session["user"]})
        record = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})
        for key, value in record.items():
            # if key and value is not None:
            print(key)
            print(value)
        
        if existing_user:
            
            edited = {
                "email": request.form.get("inputEmail").lower(),
                "password": generate_password_hash(
                    request.form.get("inputPassword")),
                "firstName": request.form.get("inputFirstName").lower(),
                "lastName": request.form.get("inputLastName").lower(),
                "is_admin": is_admin,
                "user_name": request.form.get("uname").lower(),
                "address": request.form.get("inputAddress").lower(),
                "city": request.form.get("inputCity").lower(),
                "country": request.form.get("inputCountry").lower(),
                "post_code": request.form.get("postCode").lower()
            }
            mongo.db.users.update({"_id": ObjectId(id)}, edited)
            flash("Update Successful!")
            # print(f'the {record} is')
    return_edit = mongo.db.users.find_one({"_id": ObjectId(id)})
    return render_template(
        "update_profile.html", return_edit=return_edit)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("inputPassword")):
                    session["user"] = request.form.get("inputEmail").lower()
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
    return_edit = mongo.db.users.find_one(
        {"email": session["user"]})
    # print(return_edit)
    if session["user"]:
        return render_template(
            "profile.html", tasks=tasks, return_edit=return_edit)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task successfully added")
        return redirect(url_for("add_task"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "is_urgent": is_urgent,
            "due_date": request.form.get("due_date"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Task Removed")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/info")
def info():
    return render_template("info.html")


mail_settings = {
 "MAIL_SERVER": os.environ.get(
     'MAIL_SERVER'), "MAIL_PORT": os.environ.get('MAIL_PORT'),
 "MAIL_USE_TLS": False,
 "MAIL_USE_SSL": os.environ.get('MAIL_USE_SSL'),
 "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),
 "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD'),
 "SECURITY_EMAIL_SENDER": os.environ.get("SECURITY_EMAIL_SENDER")
}


app.config.update(mail_settings)
mail = Mail(app)


@app.route("/index", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with app.app_context():
            msg = Message("Hello from HIVE")
            msg.sender = os.environ.get('MAIL_USERNAME')
            msg.recipients = [request.form.get("email")]
            # message = request.form.get("message")
            msg.body = f"Email From: {msg.sender}"
            msg.html = '<b>Hello, thanks for signing up!</b> welcome to the HIVE, check us out: <a href="https://hive-human-resources.herokuapp.com/info">HIVE</a>.'
            mail.send(msg)
            flash("Email sent!")
            return redirect(url_for('index'))
            
    return render_template("index.html")


# tell the app where and when to run the app. IP & PORT Vars hidden in env.py
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


