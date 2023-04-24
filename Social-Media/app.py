from flask import Flask, render_template, request
from flask_cors import CORS
from models import get_posts, create_post


#creates a Flask application object — app
app = Flask(__name__) 

#security concerns to stop things like cross site scripting, and sql injection
CORS(app)

# Pass the required route to the decorator.
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)
    
    posts = get_posts()

    #passes get_posts() to template for display on web page
    return render_template('index.html', posts=posts)


# if this file is selected to run, execute it, otherwise don't
if __name__ == '__main__':
    app.run(debug=True)
