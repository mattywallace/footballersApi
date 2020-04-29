from flask import Flask, jsonify

DEBUG=True
PORT=8000

app = Flask(__name__) # instantiateing the flask class 

# these are where the routes go
# the first should always be, by convention, a hello world 

@app.route('/')
def hello():
	return "Cheeky Footballers"
@app.route('/test_json')
def get_json():
	return jsonify(['hello', 'hi', 'hey'])

if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)