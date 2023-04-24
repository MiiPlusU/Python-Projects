
STEP 1
from flask import Flask, render_template, request
from flask_cors import CORS
from models import get_posts, create_post

STEP 2
create flask object

STEP 3
add a decorator to flask object and pass in the route '/' and methods get and post

STEP 4
create a view function defining how to handle http request calls, get should pass, post should
retrieve the name and post form data and assign them to a variable, then pass them as a function
to create posts. The posts should then be posted using a not defined get_posts funcition and assigned
to a posts variable

STEP 5
render html

step 6
if name = main, run app, with debugging on


Tips
flask is a python web framework that makes it easy to get a website up and running very easily
and allows us to create a server and render html

Requirements
$pip3 freeze > requirements.txt #installs requirements
pip install -r requirements.txt

Database
each post is a new row in your database and it is your primary key that auto increments
we need the name of the poster and content of the post
Not null means return an error if null
$sqlite3 database.db < schema.sql   creates database.db using schema.sql
sqllite3 is a light version of mysql thats built in with python

Server
Now we need to create the server
Full stack app
Front end: view (info most often comes from a database)
Server: from view the user makes requests to server, server grabs that out of db, pulls it back, sends it to user, server is middle man, pulls info from db, makes changes, send to front end for user view
Database
server endpoint is the same as route '/home'
when you make a request to see any webpage, that is a get request
CRUD: how to send and receive data put, post,delete

Flask
a view function is a route that maps to a function
a view/handler function is a function binded by a decorator
a decorator is a function that adds additional functionality to a function or class
ie @app.route('/', methods=['GET', 'POST'])
Flask always looks in a directory called templates to display your templates to user
{% for post in posts %}
{} is used to write python
{{}} is used to render python to screen
this is special syntax unique to python templating for html with flask, writing raw python in html to render things
{% endfor %} The {% endfor %} is a template tag in the Jinja2 templating language (which is used by Flask) that marks the end of a for loop