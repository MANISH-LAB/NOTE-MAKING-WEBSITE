from distutils.log import Log
from flask import Flask ,Blueprint
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME="Notemake.db"

def create_app():
  app=Flask(__name__)
  app.config['SECRET_KEY']="manishitis"
  app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
  db.init_app(app)

  
  from .auth import auth
  from .views import views

  app.register_blueprint(views,url_prefix="/")
  app.register_blueprint(auth,url_prefix="/")

  from . import models
  create_database(app)

  login_manager= LoginManager()
  login_manager.login_view='auth.login'
  login_manager.init_app(app)
  @login_manager.user_loader
  def load_user(id):
    return models.User.query.get(int(id))
  return app
def create_database(app):
  if not os.path.exists('website/'+"DB_NAME"):
    with app.app_context():
        db.create_all()
    print("databae created!")