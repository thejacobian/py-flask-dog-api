from flask import jsonify, Blueprint

from flask_restful import Resource, Api

import models

## view functions
class DogList(Resource):
  def get(self):
    return jsonify({'dogs': [{'name': 'Archie'}]})


class Dog(Resource):
  def get(self, id):
    return jsonify({'name': 'Archie'})

  def put(self, id):
    return jsonify({'name': 'Archie'})

  def delete(self, id):
    return jsonify({'name': 'Archie'})

# setting up a module of view functions to attack to the flask app
dogs_api = Blueprint('resources.dogs', __name__)

# instantiating our api from blueprint
api = Api(dogs_api)
api.add_resource(
  DogList,
  '/dogs',
  endpoint='dogs'
)
api.add_resource(
  Dog,
  '/dogs/<int:id>',
  endpoint='dog'
)