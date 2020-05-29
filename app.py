import os
from os import path
from flask import Flask, render_template, url_for, redirect, request
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import smtplib

if path.exists("env.py"):
  import env 

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mattie@jakusz.org'
app.config['MAIL_PASSWORD'] = '@Qu4n74sst1c'
app.config['MAIL_DEBUG'] = True
app.config["MAIL_DEFAULT_SENDER"] = 'bloobsky@gmail.com'
mail = Mail(app)


app.config["MONGO_DBNAME"] = 'complain-it'
app.config["MONGO_URI"] = os.getenv("MONGOSRC")

mongo = PyMongo(app)



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Home")

@app.route('/search_for')
def search_for():
    return render_template('search_for.html', title="Search for complained jobs")

@app.route('/complain')
def complain():
    return render_template('complain.html', title="Complain a job")

@app.route('/works')
def works():
    return render_template('works.html', title="How it works")

@app.route('/faq')
def faq():
    return render_template('faq.html', title="Frequently Asked Questions")

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title="Privacy Policy")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', title="Contact Us")
    

@app.route('/directions')
def directions():
    return render_template('directions.html', title="Directions")

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
