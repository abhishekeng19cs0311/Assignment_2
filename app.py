from flask import Flask, render_template, redirect, request, url_for, session, flash
import pyrebase
import os

config = {
    "apiKey": "AIzaSyAk8qf91oQFGrVUPyndM8pQGD-8F4cTXZs",
    "authDomain": "assignment2-d9330.firebaseapp.com",
    "projectId": "assignment2-d9330",
    "storageBucket": "assignment2-d9330.appspot.com",
    "messagingSenderId": "260789670034",
    "appId: 1:260789670034": "web:629080fc3aad3e09dbd64b",
    "databaseURL": "https://assignment2-d9330-default-rtdb.asia-southeast1.firebasedatabase.app/",
}

# #init Firebase
firebase = pyrebase.initialize_app(config)
# #auth instance
auth = firebase.auth()
# #Real-time databasename
db = firebase.database()
# #secret key for the session


# instance of flask.
app = Flask(__name__)
# secret key for the session
app.secret_key = os.urandom(24)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']

        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template("index.html")
        except:
            return render_template("login.html", message="Wrong Credentials")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form['name-signup']
        email = request.form['email-signup']
        password = request.form['pass-signup']

        try:
            auth.create_user_with_email_and_password(email, password)
            return render_template("index.html")
        except:
            return render_template("login.html")
    return render_template("login.html")


# Run main script
if __name__ == '__main__':
    app.run(debug=True)
