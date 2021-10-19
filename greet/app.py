from flask import Flask
import flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    '''returns welcome'''
    return 'Welcome'

@app.route('/welcome/home')
def welcome_home():
    '''returns welcome home'''
    return 'Welcome Home'

@app.route('/welcome/back')
def welcome_back():
    '''returns welcome back'''
    return 'Welcome Back'
