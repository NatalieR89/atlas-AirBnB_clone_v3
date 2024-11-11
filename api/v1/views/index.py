#!/usr/bin/python3

'''module'''


from api.v1.views import app_views
from flask import jsonify

# Define a route on the `app_views` object
@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON response indicating the status of the API."""
    return jsonify({"status": "OK"})

def get_stats():
    """
    Retrieves the number of each object by type.
    """
    # Define the models to count
    model_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    # Return the counts as JSON
    return jsonify(model_counts)
