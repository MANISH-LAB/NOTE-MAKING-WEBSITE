from flask import Flask ,Blueprint
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
DB_NAME=""

def create_app():
  app=Flask(__name__)
  app.config['SECRET_KEY']="manishitis"

  from .auth import auth
  from .views import views

  app.register_blueprint(views,url_prefix="/")
  app.register_blueprint(auth,url_prefix="/")

  return app