from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.secret_key = "wassup"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dojosninjas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app) 
migrate = Migrate(app, db)