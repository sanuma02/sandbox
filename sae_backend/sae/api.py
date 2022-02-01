import config
from sae import app
from flask import request, jsonify
from sae.data_model.db import DataModel as data_model
from sae.data_model.service_model import ServiceModel as sm


client = data_model()
service_collection = client.get_db()[config.SERVICE_CO]
service_model = sm(service_collection)


@app.route("/")
def home():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'api_version': 'v1.0',
        'status': '200',
        'data': 'Welcome to the Flask API'
    }
    resp = jsonify(message)
    return resp


@app.route("/api/v1/services", methods=['GET'])
def fetch_users():
    """
       Function to fetch the users.
       """
    try:
        query = {}
        result = service_model.query_service(query)
        if result:
            response = {
                'api_version': 'v1.0',
                'status': '200',
                'data': result
            }
            return jsonify(response)
        
    except Exception as e:
        print(e)
        return "", 500


@app.route("/api/v1/test_service", methods=['POST'])
def test_service():
    """
       Function to fetch the users.
       """
    try:
        app.logger.debug('Headers: %s', request.headers)
        app.logger.debug('Body: %s', request.get_data())
        data = request.json
        if data:
            app.logger.debug('data: %s', data)
        return jsonify(data)
        
    except Exception as e:
        print(e)
        return "", 500