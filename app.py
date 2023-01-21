from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_migrate import Migrate
import json
from pprint import pprint
from random import randint as rd, choice as ch
import os

from backend.database import *

app = Flask(__name__)
app.config.from_object('backend.config')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
db = db_setup(app)
migrate = Migrate(app, db)

from backend.routes import *

if __name__ == '__main__':
    app.run()