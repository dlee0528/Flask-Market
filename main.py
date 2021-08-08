from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'



@app.route('/about')
def about_pagee():
    return '<h1>About Pageee</h1>'