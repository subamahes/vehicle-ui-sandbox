from flask import Flask,render_template, request
import json

import flask

app = Flask(__name__,template_folder="templates")

@app.route("/")
def hello():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	data = request.get_json() # retrieve the data sent from JavaScript
	# process the data using Python code
	result = data
	body_json = json.dumps(result, sort_keys=True, default=str, indent=4)
	response = flask.make_response(body_json)
	response.mimetype = 'application/json'
	return response

if __name__ == '__main__':
	app.run(debug=True)
