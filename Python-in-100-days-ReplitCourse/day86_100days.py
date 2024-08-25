import os

from flask import Flask, redirect, request, session
from replit import db

app = Flask(__name__, static_url_path="/static")
app.secret_key = os.urandom(24)

db["user"] = {"username": "david", "password": "Baldy1"}

def getBlogs():
  entry = ""
  with open("entry.html", "r") as f:
    entry = f.read()
  keys = db.keys()
  keys = list(keys)
  content = ""
  for key in reversed(keys):
    thisEntry = entry
    if key != "user":
      thisEntry = thisEntry.replace("{title}", db[key]["title"])
      thisEntry = thisEntry.replace("{date}", db[key]["date"])
      thisEntry = thisEntry.replace("{body}", db[key]["body"])
      content += thisEntry
  return content


@app.route('/')
def index():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  with open("blog.html", "r") as f:
    page = f.read()
  page = page.replace("{content}", getBlogs())
  return page


@app.route('/loginForm')
def loginForm():
  if session.get("user"):
    return redirect("/edit")
  page = ""
  with open("login.html", "r") as f:
    page = f.read()
  return page


@app.route('/login', methods=["POST"])
def login():
  if session.get("user"):
    return redirect("/edit")
  form = request.form
  if form["username"] == db["user"]["username"] \
      and form["password"] == db["user"]["password"]:
    # Note this is not secure, in a real application this would be a signed message.
    session["user"] = True
    return redirect("/edit")
  else:
    return redirect("/loginForm")


@app.route("/edit")
def edit():
  if not session.get("user"):
    return redirect("/")
  page = ""
  with open("edit.html", "r") as f:
    page = f.read()
  page = page.replace("{content}", getBlogs())
  f.close()
  return page


@app.route("/add", methods=["POST"])
def add():
  form = request.form
  entry = {"title": form["title"], "date": form["date"], "body": form["body"]}
  db[form["date"]] = entry
  return redirect("/edit")


@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")


app.run(host='0.0.0.0', port=81)


##########blog.html###########
"""
<html>

<head>
  <title>David's Blog</title>
  <link rel="stylesheet" href="/static/style.css" </head>

<body>
  <h1>David's Blog</h1>
  <button type="button" onClick="location.href='/loginForm'">Log in</button>
  {content}


</body>

</html>

"""

##################edit.html###############

"""
<html>

<head>
  <title>David's Blog</title>
  <link rel="stylesheet" href="/static/style.css" </head>

<body>
  <h1>David's Blog</h1>
  <button type="button" onClick="location.href='/logout'">Log out</button>
  <form method="post" action="/add">
    <p>Title: <input type="text" name="title"></p>
    <p>Date: <input type="date" name="date"></p>
    <p>Body Text: <input type="text" name="body"></p>
    <button type="submit">Save</button>
    <hr>
    {content}

</body>

</html>

"""


############## entry.html ##############

"""
<h2>{title}</h2>
<h3>{date}</h3>
<p>{body}</p>
<hr>
"""


###########login.html###########

"""
<html>

<head>
  <title>David's Blog</title>
  <link rel="stylesheet" href="/static/style.css" </head>

<body>
  <form method="post" action="/login">
    <p>Username: <input type="text" name="username" required></p>
    <p>Password: <input type="password" name="password" required></p>
    <button type="submit">Log in</button>
  </form>
</body>

</html>
"""


