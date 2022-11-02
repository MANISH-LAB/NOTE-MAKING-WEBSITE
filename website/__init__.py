from flask import Flask ,Blueprint
def create_app():
  app=Flask('__name__')
  app.config['SECRET_KEY']="manishitis"
  return app