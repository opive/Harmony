import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import sys
print(sys.path)

app = Flask(__name__)

#database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def info():
    return render_template('info.html')
    
from error_pages.handlers import error_pages


app.register_blueprint(error_pages)


import models



