import datetime

# peewee is our ORM Object Relational Model
# gives the model the power to talk to Postgres SQL
from peewee import *

DATABASE = SqliteDatabase('dogs.sqlite')

class Dog(Model):
  name = CharField()
  owner = CharField()
  breed = CharField()
  created_at = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Dog], safe=True) # safe=True prevents re-write of data on each connection
  DATABASE.close()
