from flask import jsonify, Blueprint, abort

from flask_restful import (Resource, Api, reqparse, fields, marshal,
                               marshal_with, url_for)

import models

## Marshal fields on responses
dog_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'breed': fields.String,
    'owner': fields.String,
}


class DogList(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument(
      'name',
      required=False,
      help='No dog name provided',
      location=['form', 'json']
    )
    self.reqparse.add_argument(
      'breed',
      required=False,
      help='No dog breed provided',
      location=['form', 'json']
    )
    self.reqparse.add_argument(
      'owner',
      required=False,
      help='No owner provided',
      location=['form', 'json']
    )
    super().__init__()
      
@marshal_with(dog_fields)
def get(self, id):
  try:
    dog = models.Dog.get(models.Dog.id==id)
  except models.Dog.DoesNotExist:
    abort(404)
  else:
    return (dog, 200)
  # return jsonify({'dogs': [{'name': 'Archie'}]})

@marshal_with(dog_fields)
def put(self, id):
  args = self.reqparse.parse_args()
  query = models.Dog.update(**args).where(models.Dog.id==id)
  query.execute()
  print(query, "<-- this is query")
  return (models.Dog.get(models.Dog.id==id), 200)

@marshal_with(dog_fields)
def post(self):
  args = self.reqparse.parse_args()
  print(args, 'hittingggg post')
  dog = models.Dog.create(**args)
  return dog

class Dog(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument(
      'name',
      required=False,
      help='No dog name provided',
      location=['form', 'json']
    )
    self.reqparse.add_argument(
      'breed',
      required=False,
      help='No dog breed provided',
      location=['form', 'json']
    )
    self.reqparse.add_argument(
      'owner',
      required=False,
      help='No owner provided',
      location=['form', 'json']
    )

    super().__init__()

  @marshal_with(dog_fields)
  def get(self, id):
    try:
      dog = models.Dog.get(models.Dog.id==id)
    except models.Dog.DoesNotExist:
      abort(404)
    else:
      return (dog, 200)
    # return jsonify({'dogs': [{'name': 'Archie'}]})

  @marshal_with(dog_fields)
  def put(self, id):
    args = self.reqparse.parse_args()
    query = models.Dog.update(**args).where(models.Dog.id==id)
    query.execute()
    print(query, "<-- this is query")
    return (models.Dog.get(models.Dog.id==id), 200)

  @marshal_with(dog_fields)
  def post(self):
    args = self.reqparse.parse_args()
    print(args, 'hittingggg post')
    dog = models.Dog.create(**args)
    return dog

    def delete(self, id):
      return jsonify({'name': 'Archie'})

dogs_api = Blueprint('resources.dogs', __name__)
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