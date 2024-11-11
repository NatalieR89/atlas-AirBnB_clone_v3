#!/usr/bin/python3

'''module'''


from api.v1.views import app_views
from flask import jsonify

# Define a route on the `app_views` object
@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON response indicating the status of the API."""
    return jsonify({"status": "OK"})
