from flask_app import app
from flask_app.models import dojo, ninja
from flask import render_template, request, redirect

@app.route('/ninjas')
def show_ninjas():
    return render_template("ninja.html", dojos = dojo.Dojo.get_all_dojos())

@app.route('/ninjas/create', methods = ['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')