




Tips
flask is a python web framework that makes it easy to get a website up and running very easily
and allows us to create a server and render html

Requirements
$pip3 freeze > requirements.txt #installs requirements

Database
each post is a new row in your database and it is your primary key that auto increments
we need the name of the poster and content of the post
Not null means return an error if null
$sqlite3 database.db < schema.sql   creates database.db using schema.sql