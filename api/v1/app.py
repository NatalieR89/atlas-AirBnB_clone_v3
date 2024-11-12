#!/usr/bin/python3

'''Flask API module with CORS enabled'''

from flask import Flask, jsonify, Blueprint
from flask_cors import CORS  # Import CORS
from models import storage
from api.v1.views import app_views
import os
from os import getenv

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for all routes on the server,
# allowing all origins (especially 0.0.0.0 for local development)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register the blueprint for API views
app.register_blueprint(app_views)


# Define teardown_appcontext to close storage after each request
@app.teardown_appcontext
def teardown_db(exception):
    """Method to close storage after each request."""
    storage.close()


# Define a custom 404 error handler
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors by returning a JSON response."""
    return jsonify({"error": "Not found"}), 404


# Example route (optional, for testing purposes)
@app.route('/')
def index():
    """Route to test API is working."""
    return jsonify({"message": "Welcome to the API!"})


if __name__ == "__main__":
    """ Set host, port, debug mode from enviorn variables or defaults """
    HBNB_API_HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    HBNB_API_PORT = getenv('HBNB_API_PORT', 5000)
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT,
            threaded=True, debug=True)

    # Run the Flask app
    app.run(host=host, port=port, threaded=True, debug=debug)
