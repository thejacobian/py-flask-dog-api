from flask import Flask, g
import models

# due to __init__.py we can import the module below
from resources.users import users_api
from resources.dogs import dogs_api
from flask_cors import CORS
from flask_login import LoginManager
login_manager = LoginManager()
## sets up our login for the app

import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

CORS(dogs_api, origins=["http://localhost:3000"], supports_credentials=True)
CORS(users_api, origins= ["http://localhost:3000"], supports_credentials=True)

# url prefix to begin each route
app.register_blueprint(dogs_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

# default/home/index route
@app.route('/') #decorator @
def index():
  return 'Hello, World!'

if __name__ == '__main__':
  models.initialize()
  app.run(debug=config.DEBUG, port=config.PORT)
