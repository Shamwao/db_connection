from flask_app import app
from flask_app.controllers import dojos, ninjas

app.secret_key= "Domo Airgato Mister Roboto"

if __name__ == "__main__":
    app.run(debug=True)