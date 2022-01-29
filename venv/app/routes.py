from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gautam'}
    posts = [
        {
            'author': {'username' : 'Ram'},
            'body': 'Nice weather'
        },
        {
            'author': {'username' : 'Sandip'},
            'body': 'Very nice movie'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)

