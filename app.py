from flask import Flask, jsonify, render_template

app = Flask(__name__)
PORT = 5000

# default/home route
@app.route('/') #decorator @
def index():
  return 'Hello, World!'

@app.route('/json')
def dog():
  return jsonify(name="Frankie", age=8)

@app.route('/sayhi/<username>')
def hello(username):
  return "Hello {}".format(username)

@app.route('/greeting')
def home():
  return render_template("index.j2", greeting="something")

if __name__ == '__main__':
    app.run(debug=True, port=PORT)
