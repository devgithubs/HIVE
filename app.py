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


# create object of class
class DateForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d',
                          validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d',
                        validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')


# additional configuration
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")  # grabs DB name
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")  # connection string
app.secret_key = os.environ.get("SECRET_KEY")  # required for flask security


# create instance of pymongo and pass it the flask app
mongo = PyMongo(app)


# route for main index page of app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# route for registration page of app
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        is_admin = "on" if request.form.get("is_admin") else "off"
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})

        if existing_user:
            flash("User already exists")
            return redirect(url_for("register"))

        ent_base = {
            "email": request.form.get("inputEmail").lower(),
            "title": "Title",
            "salary": "0",
            "holidays": "20",
            "bonus": "0"
            }
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
        mongo.db.position.insert_one(ent_base)
        session["user"] = request.form.get("inputEmail")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# route for edit profile page of app
@app.route("/update_profile/<id>", methods=["GET", "POST"])
def update_profile(id):
    if request.method == "POST":
        is_admin = "on" if request.form.get("is_admin") else "off"
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})

        # record = mongo.db.users.find_one(
        #     {"email": request.form.get("inputEmail").lower()})

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

    return_edit = mongo.db.users.find_one({"_id": ObjectId(id)})
    return render_template(
        "update_profile.html", return_edit=return_edit)


# route for login page of app
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})

        if existing_user:
            if check_password_hash(
                                    existing_user["password"],
                                    request.form.get("inputPassword")):
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


# route for profile page of app
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    cur_hols = mongo.db.position.find_one({"email": session["user"]})
    new_entitlements = mongo.db.position.find_one({"email": session["user"]})
    tasks = list(mongo.db.tasks.find())
    ents_base = mongo.db.position.find_one({"email": session["user"]})
    return_edit = mongo.db.users.find_one(
        {"email": session["user"]})

    if session["user"]:
        return render_template(
            "profile.html",
            tasks=tasks,
            return_edit=return_edit,
            cur_hols=cur_hols,
            new_entitlements=new_entitlements,
            ents_base=ents_base
        )

    return redirect(url_for("login"))


# route for logout function of app
@app.route("/logout")
def logout():
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# route for add task page and function of app
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
            "task_assign": request.form.get("task_assign"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task successfully added")
        return redirect(url_for("add_task"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)


# route for edit task fucntion and page of app
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
            "task_assign": request.form.get("task_assign"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully updated")

    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_task.html", task=task, categories=categories)


# route for delete task function of app
@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    return redirect(url_for("profile", username=session["user"]))


# route for info page of app
@app.route("/info")
def info():
    return render_template("info.html")


# getting and setting the vars for the mail settings
mail_settings = {
 "MAIL_SERVER": os.environ.get(
     'MAIL_SERVER'), "MAIL_PORT": os.environ.get('MAIL_PORT'),
 "MAIL_USE_TLS": False,
 "MAIL_USE_SSL": os.environ.get('MAIL_USE_SSL'),
 "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),
 "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD'),
 "SECURITY_EMAIL_SENDER": os.environ.get("SECURITY_EMAIL_SENDER")
}


# updating the mail settings vars to app config
app.config.update(mail_settings)
# creating instance of Mail and passing the app
mail = Mail(app)


# route for handling mail on main index page of app
@app.route("/index", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with app.app_context():
            msg = Message("Hello from HIVE")
            msg.sender = os.environ.get('MAIL_USERNAME')
            msg.recipients = [request.form.get("email")]
            msg.body = f"Email From: {msg.sender}"
            msg.html = '<b>Hello, thanks for signing up!</b> \
            welcome to the HIVE, check us out: \
            <a href="https://hive-human-resources.herokuapp.com/info"> \
            HIVE</a>.'
            mail.send(msg)
            flash("Email sent!")
            return redirect(url_for('index'))

    return render_template("index.html")


# route for handling mail on info page of app
@app.route("/info", methods=["GET", "POST"])
def info_contact():
    if request.method == "POST":
        with app.app_context():
            msg = Message("Hello from HIVE")
            msg.sender = os.environ.get('MAIL_USERNAME')
            msg.recipients = [request.form.get("email")]
            msg.body = f"Email From: {msg.sender}"
            msg.html = '<b>Hello, thanks for signing up!</b> \
            welcome to the HIVE, check us out: \
            <a href="https://hive-human-resources.herokuapp.com/info"> \
            HIVE</a>.'
            mail.send(msg)
            flash("Email sent!")
            return redirect(url_for('info'))

    return render_template("info.html")


# route for handling annual leave page of app
@app.route("/annual_leave/<hol_id>", methods=["GET", "POST"])
def annual_leave(hol_id):
    form = DateForm(meta={'csrf': False})
    if request.method == "POST":
        get_hols = mongo.db.position.find_one({"email": session["user"]})
        print(get_hols)
        if get_hols is None:
            print("None")

        elif int(get_hols["holidays"]) <= 0:
            flash(
                "You have no Holidays available to take, \
                 contact your HR department.")
        elif form.validate_on_submit():
            session['startdate'] = form.startdate.data
            session['enddate'] = form.enddate.data

            delta = session['enddate'] - session['startdate']
            delta = delta.days
            new_hols = int(get_hols["holidays"]) - delta
            print(new_hols)
            hol_update = {"$set": {"holidays": new_hols}}
            mongo.db.position.update_one({"_id": ObjectId(hol_id)}, hol_update)
            flash(f"You have booked {delta} day(s) off!")

    cur_hols = mongo.db.position.find_one({"_id": ObjectId(hol_id)})
    print(cur_hols["email"])
    return render_template(
        'annual_leave.html', form=form, cur_hols=cur_hols)


# route for handling edit entitlements page and function
@app.route("/edit_entitlements/<entitlement_id>", methods=["GET", "POST"])
def edit_entitlements(entitlement_id):
    if request.method == "POST":
        user_entitled = mongo.db.users.find_one(
            {"email": request.form.get("inputEmail").lower()})

        if user_entitled:
            entitlement = {
                "email": request.form.get("inputEmail").lower(),
                "title": request.form.get("inputTitle").lower(),
                "salary": request.form.get("inputSalary").lower(),
                "holidays": request.form.get("inputHolidays").lower(),
                "bonus": request.form.get("inputBonus").lower()
            }
            mongo.db.position.update_one(
                {"email": request.form.get("inputEmail").lower()},
                {"$set": entitlement})
            flash('Profile updated')

    name = mongo.db.users.find_one({"email": session["user"]})
    new_entitlements = mongo.db.position.find_one(
        {"_id": ObjectId(entitlement_id)})
    return render_template(
        "edit_entitlements.html", new_entitlements=new_entitlements, name=name)


# tell the app where and when to run the app. IP & PORT Vars hidden in env.py
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
