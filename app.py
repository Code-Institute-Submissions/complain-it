import os
from os import path
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if path.exists("env.py"):
    import env 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'complain_it'
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

@app.route('/cat')
def cat():
    return render_template('cat.html', title="Categories", categories=mongo.db.categories.find())

@app.route('/edit_cat/<category_id>')
def edit_cat(category_id):
    return render_template('editcat.html', category=mongo.db.categories.find_one({"_id": ObjectId(category_id)}))

@app.route('/update_cat/<category_id>', methods=["POST"])
def update_cat(category_id):
    mongo.db.categories.update({'_id': ObjectId(category_id)},
    {'category_name': request.form.get('category_name')})
    return redirect(url_for('cat'))

@app.route('/delete_cat/<category_id>')
def delete_cat(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('cat'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
