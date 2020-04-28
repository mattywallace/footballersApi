from flask import Flask

DEBUG=True
PORT=8000

app = Flask(__name__) # instantiateing the flask class 

# these are where the routes go
# the first should always be, by convention, a hello world 

@app.route('/')
def hello():
	return "Cheeky Footballers"

if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)