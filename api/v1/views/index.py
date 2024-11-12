#!/usr/bin/python3
'''module'''


from flask import jsonify, Blueprint
from api.v1.views import app_views
from models import storage
# Assuming storage is initialized in models/__init__.py


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Returns JSON """
    return jsonify({'status': 'OK'})


@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
    """
    Retrieves the number of each object type by calling storage.count()
    """
    objects = {"amenities": 'Amenity', "cities": 'City',
               "places": 'Place', "reviews": 'Review',
               "states": 'State', "users": 'User'}
    stats = {}
    try:
        for key, value in objects.items():
            stats[key] = storage.count(value)
            print(f"Count of {value}: {stats[key]}")
            return jsonify(stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500 