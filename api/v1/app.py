#!/usr/bin/python3

'''Flask API module with CORS enabled'''

from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from models import storage
from api.v1.views import app_views
import os

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for all routes on the server, allowing all origins (especially 0.0.0.0 for local development)
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
    # Set the host, port, and debug mode from environment variables or default values
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    
    # Run the Flask app
    app.run(host=host, port=port, threaded=True, debug=debug)
