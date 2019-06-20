from flask import jsonify, Blueprint, abort

from flask_restful import (Resource, Api, reqparse, fields, marshal,
                               marshal_with, url_for)

import models

## define fields on responses
dog_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'breed': fields.String,
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
            help='No course dog breed provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'owner',
            required=False,
            help='No  owner provided',
            location=['form', 'json']
        )
        super().__init__()
        
    def get(self):
        return jsonify({'dogs': [{'name': 'Archie'}]})

    def post(self):
        args = self.reqparse.parse_args()
        print(args, 'hittingggg')
        dog = models.Dog.create(**args)
        return jsonify({'dogs': [{'name': 'Archie'}]})


class Dog(Resource):
    def get(self, id):
        return jsonify({'name': 'Archie'})

    def put(self, id):
        return jsonify({'name': 'Archie'})

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