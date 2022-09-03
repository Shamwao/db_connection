from users import User
from flask import Flask, render_template, request, redirect


app= Flask(__name__)


@app.route("/")
def pushto():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template("users.html", users = User.get_all())
    
@app.route("/user/new")
def new():
    return render_template('new_user.html')

@app.route("/user/create", methods = ['POST'])
def create():
    User.save(request.form)
    return redirect("/users")

@app.route("/user/<int:id>")
def read_one(id):
    data = {
        "id": id
    }
    User.get_one(data)
    return render_template("read_one.html", user = User.get_one(data))

@app.route("/user/destroy/<int:id>")
def destroy(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect ("/users")

@app.route("/user/edit/<int:id>")
def edit_one(id):
    data = {
        "id": id
    }
    return render_template ("edit.html", user=User.get_one(data))

@app.route('/user/update', methods = ['POST'])
def update():
    User.update(request.form)
    return redirect ("/users")

if __name__ == "__main__":
    app.run(debug=True)

