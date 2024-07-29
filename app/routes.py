from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, DashboardForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = DashboardForm()
    if form.validate_on_submit():
        pass
    return render_template('dashboard.html', title='Dashboard', form=form)


@app.route('/documentation')
def documentation():
    return render_template('documentation.html', title='Developer Documentation')