from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect

@app.route("/")
def index():
    return redirect ("/dojos") 

@app.route("/dojo/create", methods = ['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect ("/")

@app.route("/dojos")
def show_dojos():
    return render_template("index.html", dojos = Dojo.get_all_dojos())

@app.route('/dojos/<int:id>')
def dojo_roster(id):
    data = {
        "id": id
    }
    return render_template ("dojo.html", dojo = Dojo.get_dojo_with_ninjas(data))