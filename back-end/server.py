#these are all required imports login api
from enum import unique
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

#creates unique id
def CreateUUID ():
    return uuid4().hex


#create model class user for database to store email and password
class User (db.Model):
       #table name
       __tablename__ = "users"
       #to generate unique id using createUUID class
       id= db.Column(db.String (32), unique=True, primary_key=True, default=CreateUUID)
       #create email column in table unique emails
       email= db.Column(db.String(355), unique=True)
       #creates a password column in table with should not be null.
       password = db.Column(db.String(), nullable=False)


#Next, we want configure backend with sql alchemy attributes which shows whats happening in the database as well as create db in the current folder.
class AppConfiguration:
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      SQLACLCHEMY_ECHO = True
      SQLALCHEMY_DATABASE_URI= r"sqlite:///./db.sqlite"


#to start the app/server
app = Flask (__name__)
app.config.from_object (AppConfiguration)
db.init_app(app)


#now to set up the registeration
#set the url to /registeration with the post method
@app.route("/register", methods=["POST"])
def RegisterUser():
    #We store the incoming data in a variable as a json data
    user_data = request.get_json();
    # we then create another variable and call the user => db model and pass the json data into it.
    # recall that user model as two column email and password
    # and we easily set each by parsing the JSON object.
    user = User(email=user_data["email"], password=user_data["password"])
    #add the user the db and commit.
    db.session.add(user)
    db.session.commit()

    # we can return, 201 status which is success
    return "done", 201



""" this alows us to use the server without having it online"""
with app.app_context():
	db.create_all()

if __name__ == "___main__":
	app.run(debug=True)