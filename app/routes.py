from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    user = {'username': 'Miguel'}
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/template')
def home():
    return render_template('template.html')