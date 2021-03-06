#!flask/Source/python

from flask import Flask, jsonify,request 
from config import Config

config=Config()
cursor = config.get_cursor()


app = Flask('app')
@app.route('/')
def index():
  return 'Hello World'

@app.route('/user', methods=['GET'])
def get_users():
  
  cursor.execute("SELECT * FROM user")
  result = cursor.fetchall()
  return jsonify(result)

@app.route('/register', methods=['POST'])
def register_user():
  result = request.get_json()
  
  # get data from the request object

  name = result['name']
  email = result['email']
  password = result['password']

  # insert data to table
  query = "INSERT INTO user Values (%s, %s, %s, %s, NOW())"
  values = (3, name, email, password)
  cursor.execute(query, values)

  return jsonify(result)

if __name__ =='__main__':
  app.run( debug=True)