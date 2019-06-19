from flask import Flask, g
import models

# due to __init__.py we can import the module below
from resources.dogs import dogs_api

PORT = 5000
DEBUG = True

app = Flask(__name__)

# url prefix to begin each route
app.register_blueprint(dogs_api, url_prefix='/api/v1')

@app.before_request
def before_request():
  """connect to the database before each request"""
  g.db = models.DATABASE
  g.db.connect()

@app.after_request
def after_request(response):
  """close the database connection after each request"""
  g.db.close()
  return response

# default/home/index route
@app.route('/') #decorator @
def index():
  return 'Hello, World!'

if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)
