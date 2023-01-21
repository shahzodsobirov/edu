from .database import *
from app import *


@app.route('/home')
def hello_world():  # put application's code here
    return render_template("home.html")
