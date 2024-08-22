from flask import Flask

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
  return "Go to /portfolio or /linktree, not here!"


@app.route('/portfolio')
def portfolio():
  page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href="/static/css/portfolio.css" rel="stylesheet" type="text/css" />
</head>

<body>

  <h1>Ashim Portfolio</h1>
  <h2>Day 56 </h2>
  <p>Day 56 was about using csv reading and file and folder manipulation to make 100 files in dozens of folders.</p>

  <script src="script.js"></script>

</body>

</html>
"""
  return page


@app.route('/linktree')
def linktree():
  page = f"""<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="static/css/linktree.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <img src="static/images/my_img.jpg" width="50px">
<h1>Ashim Nepal</h1>
  <p class="about">Hey its Ashim!</p>
  <h3>Socials</h3>
  <ul>
    <li><a href="">Twitter (@my twitter)</a></li>
    <li><a href="">YouTube (@my_youtube)</a></li>
    <li><a href="">replit (@my_replit)</a></li>
  </ul>




  <script src="script.js"></script>

</body>

</html>
"""
  return page


app.run(host='0.0.0.0', port=81)
