from flask import Flask, render_template, request, redirect, url_for, Response, session, make_response, jsonify
from src.common.database import Database
from src.models.burger import Burger

app = Flask(__name__)
app.secret_key = "libby"

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def home_template():
    burgers = Burger.findAll_mongo()
    return render_template('index.html', burgers=burgers)

# new burger
@app.route('/burger/new', methods=['POST'])
def create_new_recipe():
    name = request.form['burger']
    new_burger = Burger(name)
    print(new_burger)
    new_burger.save_burger()
    return redirect(url_for('home_template'))

# update burger
@app.route('/burger/<string:_id>', methods=['POST'])
def update_recipe(_id):
    # id = "ObjectId(" + '"' + _id + '")'
    eaten = {"eaten": True}
    # print(id, eaten)
    Burger.update_burger(id=_id, data=eaten)
    return redirect(url_for('home_template'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
