from flask_sqlalchemy import SQLAlchemy
from flask import Flask


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    #initializing flask extensions
    db.init_app(app)