from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SECRET_KEY'] = '634a0cf5cbd636bc98b1228b'
db = SQLAlchemy(app)

from project import routes

''' creation db 
flask shell
db.create_all()
db.drop_all()
'''