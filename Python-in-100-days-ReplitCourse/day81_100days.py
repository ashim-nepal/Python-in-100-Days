from flask import Flask, request

app = Flask(__name__)


@app.route("/robot", methods=["POST"])
def robot():
    form = request.form
    if form['metal'] == "Yes":
        return "You're a robot!"
    elif "error" in form["infinity"].lower():
        return "You're a robot!"
    elif form["food"] == "synthetic oil":
        return "You're a robot!"
    else:
        return "Hi there fellow human"


@app.route('/')
def index():
    page = ""
    with open("form.html", "r") as f:
      page = f.read()
    return page

app.run(host='0.0.0.0', port=81)


###################Form.html######################
"""

<form method="post" action="/robot">

  <p>Are you made of metal? <input type="radio" name="metal" value="Yes"> Yes </p> <input type="radio" name="metal" value="No"> No </p>

  <p>What is infinity + 1? <input type="text" name="infinity" required></p>

  <p>Which is your favorite food? <select name="food"><option value="human food">Human food</option><option value="synthetic oil">Synthetic Oil</option></select></p>

  <button type="submit">I am not a robot</button>

</form>

"""