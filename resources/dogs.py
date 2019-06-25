from flask import jsonify, Blueprint, abort

from flask_restful import (Resource, Api, reqparse, fields, marshal,
                               marshal_with, url_for)

from flask_login import login_required, current_user
import models

## Marshal fields on responses, these are the fields we send back to the client
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
  
  def get(self):
    # models.Dog.select() ## Look up peewee queries
    # for Generating response object
    # marshal in flask
    dogs_list = [marshal(dog, dog_fields) for dog in models.Dog.select()]
    return dogs_list
    # return jsonify({'dogs': [{'name': 'Archie'}]})

  @login_required
  @marshal_with(dog_fields)
  def post(self):
    args = self.reqparse.parse_args()
    print(args, 'hittingggg post')
    dog = models.Dog.create(**args)
    print(dog, "<---", type(dog))
    return (dog, 201)

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

  @login_required
  @marshal_with(dog_fields)
  def get(self, id):
    try:
      dog = models.Dog.get(models.Dog.id==id)
    except models.Dog.DoesNotExist:
      abort(404)
    else:
      return (dog, 200)
    # return jsonify({'dogs': [{'name': 'Archie'}]})

  @login_required
  @marshal_with(dog_fields)
  def put(self, id):
    args = self.reqparse.parse_args()
    query = models.Dog.update(**args).where(models.Dog.id==id)
    query.execute()
    print(query, "<-- this is query")
    return (models.Dog.get(models.Dog.id==id), 200)

  @login_required
  def delete(self, id):
    query = models.Dog.delete().where(models.Dog.id==id)
    query.execute()
    return jsonify({'message': 'resource deleted'})

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