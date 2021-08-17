import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)

# REGISTER CODE
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "user_type": request.form.get("user_type"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        session["user_type"] = request.form.get("user_type").lower()
        flash("Registration Successful!")
        return redirect(url_for("registered", username=session["user"], user_type=session["user_type"]))

    return render_template("register.html")


@app.route("/registered/<username>/<user_type>", methods=["GET", "POST"])
def registered(username, user_type):
    username = session["user"]
    user_type = session["user_type"]

    print(user_type)

    if session["user"]:
        if user_type == "player":
            return render_template("create-profile.html", username=username)
        else:
            return render_template("create-scout-profile.html", username=username, user_type=user_type)

    return redirect(url_for("login"))



# LOGIN CODE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        check_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if check_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    check_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {session[username]}".format(
                            request.form.get("username")))
                        return redirect(url_for("read_profile", 
                            profilename=session["user"], username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    session.pop("user_type")
    return redirect(url_for("index"))


# PROFILE CODE
@app.route("/create-profile", methods=["GET", "POST"])
def create_profile():
    if request.method == "POST":

        username = session["user"]

        usertype = session["user_type"]

        edit_profile = {
            "name": request.form.get("name").lower(),
            "profile_pic": request.form.get("profile_pic"),
            "DOB": request.form.get("DOB").lower(),
            "current_team": request.form.get("current_team").lower(),
            "bio": request.form.get("bio").lower(),
            "gender": request.form.get("gender").lower(),
            "position": request.form.get("position"),
            "user": session["user"],
            "user_type": session["user_type"]
        }

        mongo.db.profiles.insert(edit_profile)
        flash("create Successful!")
        return redirect(url_for("read_profile", username=username))

    return render_template("create-profile.html")


@app.route("/read-profile/<username>", methods=["GET"])
def read_profile(username):
    
    query = { "user": username }

    check_profile = mongo.db.profiles.find(query)

    for x in check_profile:
        profile = {
            "name": x["name"],
            "profile_pic": x["profile_pic"],
            "DOB": x["DOB"],
            "current_team": x["current_team"],
            "bio": x["bio"],
            "gender": x["gender"],
            "position": x["position"],
            "user": username,
            "user_type": x["user_type"]
        }

    ev_query = { "player": username }

    check_events = mongo.db.events.find(ev_query)
    events = []

    for x in check_events:
        event = {
            "_id": x["_id"],
            "name": x["name"],
            "time": x["time"],
            "location": x["location"],
            "player": x["player"]
        }
        events.append(event)

    return render_template('profile.html', profile= profile, events = events)



@app.route("/edit-profile", methods=["GET", "POST"])
def edit_profile():
    query = { "user": session["user"] }

    check_profile = mongo.db.profiles.find(query)

    for x in check_profile:
        profile = {
            "name": x["name"],
            "profile_pic": x["profile_pic"],
            "DOB": x["DOB"],
            "current_team": x["current_team"],
            "bio": x["bio"],
            "gender": x["gender"],
            "position": x["position"],
            "user": x["user"],
            "user_type": x["user_type"]
        }

    return render_template("edit-profile.html", profile=profile)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    username = session["user"]
    user_type = session["user_type"]

    if session["user"] and session["user_type"]:
        return render_template("profile.html", username=username,
        user_type=user_type)

    return redirect(url_for("login"))

@app.route("/update-profile", methods=["GET", "POST"])
def update_profile():
    if request.method == "POST":

        username = session["user"]

        usertype = session["user_type"]

        update_profile = {
            "name": request.form.get("name").lower(),
            "profile_pic": request.form.get("profile_pic"),
            "DOB": request.form.get("DOB").lower(),
            "current_team": request.form.get("current_team").lower(),
            "bio": request.form.get("bio").lower(),
            "gender": request.form.get("gender").lower(),
            "position": request.form.get("position"),
            "user": session["user"],
            "user_type": session["user_type"]
        }

        mongo.db.profiles.save(update_profile)
        flash("update Successful!")
        return redirect(url_for("read_profile", username=username))


# EVENTS CODE

@app.route("/create-event", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":

        username = session["user"]

        event = {
            "name": request.form.get("name").lower(),
            "time": request.form.get("time"),
            "location": request.form.get("location").lower(),
            "player": username
        }

        mongo.db.events.insert(event)
        flash("create Event Successful!")
        return redirect(url_for("read_profile", username=username))

    return render_template("create-event.html")


@app.route("/delete-event/<event_id>")
def delete_event(event_id):

    username = session["user"]

    ev = mongo.db.events.find_one({"_id": ObjectId(event_id)})

    mongo.db.events.remove(ev)
    flash("delete Event Successful!")
    return redirect(url_for("read_profile", username=username))

    
@app.route("/edit-event/<event_id>", methods=["GET"])
def edit_event(event_id):

    ev = mongo.db.events.find_one({"_id": ObjectId(event_id)})

    event = {
        "event_id": ev["_id"],
        "name": ev["name"],
        "time": ev["time"],
        "location": ev["location"],
        "player": ev["player"]
    }

    return render_template("edit-event.html", event=event)


@app.route("/update-event/<event_id>", methods=["POST"])
def update_event(event_id):

    if request.method == "POST":

        username = session["user"]

        update_event = {
            "_id": ObjectId(event_id),
            "name": request.form.get("eventname"),
            "time": request.form.get("eventtime"),
            "location": request.form.get("eventlocation"),
            "player": session["user"],
        }

        mongo.db.events.save(update_event)
        flash("update Successful!")
        return redirect(url_for("read_profile", username=username))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
