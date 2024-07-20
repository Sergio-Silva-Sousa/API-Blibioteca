from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.database.models.livros import Livro
from app.extensions import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
db_url = os.getenv("URL_DATABASE")
app.config["SQLALCHEMY_DATABASE_URI"] =  db_url
db.init_app(app)
migrate = Migrate(app,db)
