from users import User
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


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



if __name__ == "__main__":
    app.run(debug=True)

