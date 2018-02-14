from app import app
from flask import render_template, flash, redirect

from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
