from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'guru'}
    posts = [
        {
            'author': {'username': 'sarah'},
            'body': 'A bad-ass'
        },
        {
            'author': {'username': 'jessica'},
            'body': 'Yeah, but I do not flaunt it'
        },
        {
            'author': {'username': 'luke'},
            'body': 'Sweet Christmas!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
