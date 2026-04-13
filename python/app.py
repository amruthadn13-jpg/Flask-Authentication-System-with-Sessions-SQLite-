from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)



app.secret_key = "secret123"



def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()




@app.route("/")
def home():
    return render_template("index.html", message="")




@app.route("/register", methods=["POST"])
def register():

    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        message = "Username already exists"

    else:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        message = " Registered Successfully"

    conn.close()
    return render_template("index.html", message=message)



@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user and user[2] == password:
       
        session["user"] = username
        return redirect("/dashboard")

    else:
        return render_template("index.html", message=" Invalid Login")



@app.route("/dashboard")
def dashboard():

    if "user" in session:
        return render_template("dashboard.html", user=session["user"])

    else:
        return redirect("/")


@app.route("/logout")
def logout():

    session.pop("user", None)
    return redirect("/")


app.run(debug=True)
