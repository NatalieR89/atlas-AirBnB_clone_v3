#!/usr/bin/python3

'''module'''


from flask import jsonify
from api.v1.views import app_views
from models import storage  # Assuming storage is initialized in models/__init__.py


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Returns JSON """
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """
    Retrieves the number of each object type by calling storage.count()
    """
    stats = {
        "User": storage.count("User"),
        "Place": storage.count("Place"),
        "City": storage.count("City"),
        "Amenity": storage.count("Amenity"),
        "Review": storage.count("Review"),
        "State": storage.count("State")
    }
    return jsonify(stats)
