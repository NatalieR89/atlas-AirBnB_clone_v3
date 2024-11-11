#!/usr/bin/python3

'''module'''

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# Initialize Flask application
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)

# Define teardown_appcontext to close storage
@app.teardown_appcontext
def teardown_db(exception):
    """Method to close storage after each request"""
    storage.close()

if __name__ == "__main__":
    # Set the host and port from environment variables or default values
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    # Run the Flask app
    app.run(host=host, port=port, threaded=True)
