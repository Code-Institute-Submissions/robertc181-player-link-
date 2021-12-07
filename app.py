import os
import datetime
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

###########################################################################################################


@app.route("/")
@app.route("/index")
def index():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)

###########################################################################################################

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

###########################################################################################################


@app.route("/registered/<username>/<user_type>", methods=["GET", "POST"])
def registered(username, user_type):
    username = session["user"]
    user_type = session["user_type"]

    if session["user"]:
        return render_template("create-profile.html", username=username, user_type=user_type)

    return redirect(url_for("login"))

###########################################################################################################

# LOGIN CODE


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        check_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if check_user:
            # ensure hashed password matches user input
            if check_password_hash(check_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session["user_type"] = check_user["user_type"]
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("read_profile", profilename=session["user"], username=session["user"], user_type=session["user_type"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

###########################################################################################################


@app.route("/logout")
def logout():
    # remove user from session cookie
    try:
        if session['user']:
            session.pop("user")
            session.pop("user_type")

            flash("You have been logged out")
            return redirect(url_for("index"))

    except KeyError:

        flash("please login")
        return redirect(url_for("index"))


###########################################################################################################

# PROFILE CODE
@app.route("/create-profile", methods=["GET", "POST"])
def create_profile():
    if request.method == "POST":

        username = session["user"]

        user_type = session["user_type"]

        if user_type == "player":
            # Using datetime to format date
            dtstr = request.form.get("DOB")
            dt = datetime.datetime.strptime(dtstr, '%Y-%m-%d')
            date = dt.strftime("%Y-%m-%d")
            # Populate create profile object
            create_profile = {
                "name": request.form.get("name").lower(),
                "DOB": date,
                "current_team": request.form.get("current_team").lower(),
                "bio": request.form.get("bio").lower(),
                "gender": request.form.get("gender").lower(),
                "user": session["user"],
                "user_type": session["user_type"]
            }

        else:
            # Populate event if user_type is scout
            create_profile = {
                "name": request.form.get("name").lower(),
                "bio": request.form.get("bio").lower(),
                "gender": request.form.get("gender").lower(),
                "cert": request.form.get("cert"),
                "user": session["user"],
                "user_type": session["user_type"]
            }

        mongo.db.profiles.insert(create_profile)
        flash("create Successful!")
        return redirect(url_for("read_profile", username=username, user_type=user_type))

    return render_template("create-profile.html")

###########################################################################################################


@app.route("/read-profile/<username>/<user_type>", methods=["GET", "POST"])
def read_profile(username, user_type):
    if "user" in session:

        query = {"user": username}

        check_profile = mongo.db.profiles.find(query)


        if user_type == "player":

            for x in check_profile:
                # Using datetime to format date from date picker
                dt = datetime.datetime.strptime(x["DOB"], '%Y-%m-%d')
                date = dt.strftime("%d-%m-%Y")
                # Getting profile data from mongo
                profile = {
                    "_id": x["_id"],
                    "name": x["name"],
                    "DOB": date,
                    "current_team": x["current_team"],
                    "bio": x["bio"],
                    "gender": x["gender"],
                    "user": username,
                    "user_type": x["user_type"]
                }

            ev_query = {"player": username}

            check_events = mongo.db.events.find(ev_query)
            events = []
            # Getting event data from mongo
            for x in check_events:
                if "scout" in x:
                    event = {
                        "_id": x["_id"],
                        "name": x["name"],
                        "time": x["time"],
                        "location": x["location"],
                        "player": x["player"],
                        "playername": x["playername"],
                        "scout": x["scout"]

                    }
                else:
                    event = {
                        "_id": x["_id"],
                        "name": x["name"],
                        "time": x["time"],
                        "location": x["location"],
                        "player": x["player"],
                        "playername": x["playername"]
                    }
                events.append(event)

        else:
            # Getting  watched event data from mongo if user_type is scout
            events = list(mongo.db.events.find({"scout":username}))
            
            # Getting profile data from mongo if user_type is scout
            for x in check_profile:
                profile = {
                    "_id": x["_id"],
                    "name": x["name"],
                    "bio": x["bio"],
                    "gender": x["gender"],
                    "cert": x["cert"],
                    "user": username,
                    "user_type": x["user_type"]
                }

        if request.method == "POST":
            # Finding players from mongo in search input
            query = request.form.get("query")
            players = list(mongo.db.profiles.find(
                {"name": {'$regex': query}, "user_type": "player"}))
        else:
            players = []
        return render_template('profile.html', profile=profile, events=events, players=players)

    else:

        return redirect(url_for("login"))
###########################################################################################################


@app.route("/edit-profile/<profile_id>", methods=["GET", "POST"])
def edit_profile(profile_id):

    check_profile = mongo.db.profiles.find_one({"_id": ObjectId(profile_id)})

    if session["user_type"] == "player":
        # Populate update profile object
        profile = {
            "profile_id": profile_id,
            "name": check_profile["name"],
            "DOB": check_profile["DOB"],
            "current_team": check_profile["current_team"],
            "bio": check_profile["bio"],
            "gender": check_profile["gender"],
            "user": check_profile["user"],
            "user_type": check_profile["user_type"]
        }
    else:
        # Populate profile object if user_type is scout
        profile = {
            "profile_id": profile_id,
            "name": check_profile["name"],
            "cert": check_profile["cert"],
            "bio": check_profile["bio"],
            "gender": check_profile["gender"],
            "user": check_profile["user"],
            "user_type": check_profile["user_type"]
        }

        return render_template("edit-profile.html", profile=profile)

    return render_template("edit-profile.html", profile=profile)

###########################################################################################################


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if "user" in session:

        username = session["user"]
        user_type = session["user_type"]
        profile = mongo.db.profiles.find_one({"user":username})
        # Rendering the profile 
        if session["user"] and session["user_type"]:
            return render_template("profile.html", username=username,
                                user_type=user_type, profile=profile)

    else:

        return redirect(url_for("login"))

###########################################################################################################


@app.route("/update-profile/<profile_id>", methods=["GET", "POST"])
def update_profile(profile_id):
    if request.method == "POST":

        username = session["user"]

        if session["user_type"] == "player":
            # Populate update profile object
            update_profile = {
                "_id": ObjectId(profile_id),
                "name": request.form.get("name").lower(),
                "DOB": request.form.get("DOB").lower(),
                "current_team": request.form.get("current_team").lower(),
                "bio": request.form.get("bio").lower(),
                "gender": request.form.get("gender").lower(),
                "user": session["user"],
                "user_type": session["user_type"]
            }

        else:
            # Populate update profile object user_type is scout
            update_profile = {
                "_id": ObjectId(profile_id),
                "name": request.form.get("name").lower(),
                "cert": request.form.get("cert").lower(),
                "bio": request.form.get("bio").lower(),
                "gender": request.form.get("gender").lower(),
                "user": session["user"],
                "user_type": session["user_type"]

            }

        mongo.db.profiles.save(update_profile)
        flash("update Successful!")
        return redirect(url_for("read_profile", username=username, user_type=session["user_type"]))


###########################################################################################################

# EVENTS CODE

@app.route("/create-event/<profile_id>", methods=["GET", "POST"])
def create_event(profile_id):
    if request.method == "POST":

        username = session["user"]

        pr = mongo.db.profiles.find_one({"_id": ObjectId(profile_id)})
        # Populate event object from the form
        event = {
            "name": request.form.get("name").lower(),
            "time": request.form.get("time"),
            "location": request.form.get("location").lower(),
            "player": username,
            "playername": pr["name"],
            "scout": ""
        }

        mongo.db.events.insert(event)
        flash("create Event Successful!")
        return redirect(url_for("read_profile", username=username, user_type=session["user_type"]))

    return render_template("create-event.html", profile_id=profile_id)

###########################################################################################################


@app.route("/delete-event/<event_id>")
def delete_event(event_id):

    username = session["user"]

    ev = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    # Removing event data from mongo
    mongo.db.events.remove(ev)
    flash("delete Event Successful!")
    return redirect(url_for("read_profile", username=username, user_type=session["user_type"]))

###########################################################################################################


@app.route("/edit-event/<event_id>", methods=["GET"])
def edit_event(event_id):

    ev = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    # Populate event object for the form
    event = {
        "event_id": ev["_id"],
        "name": ev["name"],
        "time": ev["time"],
        "location": ev["location"],
        "player": ev["player"],
        "playername": ev["playername"],
        "scout": ev["scout"]

    }

    return render_template("edit-event.html", event=event)

###########################################################################################################


@app.route("/update-event/<event_id>", methods=["POST"])
def update_event(event_id):

    if request.method == "POST":

        username = session["user"]

        ev = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        # Populate update event object
        update_event = {
            "_id": ObjectId(event_id),
            "name": request.form.get("eventname"),
            "time": request.form.get("eventtime"),
            "location": request.form.get("eventlocation"),
            "player": session["user"],
            "playername": ev["playername"],
            "scout": ev["scout"]
        }

        mongo.db.events.save(update_event)
        flash("update Successful!")
        return redirect(url_for("read_profile", username=username, user_type=session["user_type"]))

###########################################################################################################


@app.route("/player-profile/<player_name>", methods=["GET", "POST"])
def player_profile(player_name):

    username = session["user"]

    query = {"name": player_name}

    check_profile = mongo.db.profiles.find(query)

    for x in check_profile:
        # Format datepicker data with datetime
        dt = datetime.datetime.strptime(x["DOB"], '%Y-%m-%d')
        date = dt.strftime("%d-%m-%Y")
        # Populate player profile object
        profile = {
            "name": x["name"],
            "DOB": date,
            "current_team": x["current_team"],
            "bio": x["bio"],
            "gender": x["gender"],
            "user": username,
            "user_type": x["user_type"]
        }
    ev_query = {"playername": player_name}

    check_events = mongo.db.events.find(ev_query)
    events = []
    for x in check_events:
        if "scout" in x:
            # Populate players event object
            event = {
                "_id": x["_id"],
                "name": x["name"],
                "time": x["time"],
                "location": x["location"],
                "player": x["player"],
                "playername": x["playername"],
                "scout": x["scout"]

            }
        else:
            # Populate players event object if scout doesn't exist
            event = {
                "_id": x["_id"],
                "name": x["name"],
                "time": x["time"],
                "location": x["location"],
                "player": x["player"],
                "playername": x["playername"]
            }
        events.append(event)

    return render_template('player-profile-display.html', profile=profile, events=events)

###########################################################################################################


@app.route("/watch-event/<event_id>", methods=["GET"])
def watch_event(event_id):

    username = session["user"]

    user_type = session["user_type"]

    ev = mongo.db.events.find_one({"_id": ObjectId(event_id)})
    # Populate event object with scout
    event = {
        "_id": ObjectId(event_id),
        "name": ev["name"],
        "time": ev["time"],
        "location": ev["location"],
        "player": ev["player"],
        "playername": ev["playername"],
        "scout": username
    }
    mongo.db.events.save(event)
    flash("watching event")
    return redirect(url_for("read_profile", username=username, user_type=user_type ))
# player_name=event["player"]
###########################################################################################################


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
