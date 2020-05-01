from flask import Flask
from flask import jsonify
from flask import request

from flask_cors import CORS

from components import test_component
from components import all_strains
from components import strain_from_id
from components import symptom_from_query
from components import strain_from_symptom

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!" 

# This will just give you a simple json when you visit http://localhost:5000/jsontest
@app.route("/jsontest")
def jsontest():
    data = {'test':'success!'}
    return jsonify(data)

@app.route("/test")
def test():
    text = test_component()
    return text


# Just an example of to use text inputs in requests.
# Example: http://localhost:5000/hello?name=Lawrence%20Kimsey
@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

# http://localhost:5000/strains/all
@app.route('/strains/all')
def get_all_strains():
    data = all_strains()
    return jsonify(data)


# http://localhost:5000/strains/id/420
@app.route('/strains/id/<strainid>')
def get_strain_from_id(strainid):
    strainid = int(strainid)
    data = strain_from_id(strainid)
    return jsonify(data)


# http://localhost:5000/strains/symptom/insomnia
@app.route('/strains/symptom/<symptom>')
def get_strain_from_symptom(symptom):
    data = strain_from_symptom(symptom)
    return jsonify(data)


# http://localhost:5000/strains/query/My head hurts
@app.route('/strains/query/<query>')
def get_strain_from_query(query):
    symptom = symptom_from_query(query)
    data = strain_from_symptom(symptom)
    return jsonify(data)


# http://localhost:5000/test/My head hurts
@app.route('/test/<query>')
def get_symptom_from_query(query):
    symptom = symptom_from_query(query)
    return symptom