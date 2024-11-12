#!/usr/bin/python3

'''module'''

from flask import jsonify, request, abort, Blueprint
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from models.user import User

@app_views.route('/api/v1/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews(place_id):
    """Retrieves the list of all Review objects of a specific Place."""
    place = storage.get("Place", place_id)
    if not place:
        abort(404)
    return jsonify([review.to_dict() for review in place.reviews])


@app_views.route('/api/v1/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Retrieves a specific Review object."""
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/api/v1/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Deletes a specific Review object."""
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/api/v1/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_review(place_id):
    """Creates a Review object linked to a specific Place."""
    """ Creates a Review object """
    place = storage.get("Place", place_id)
    if not place:
        abort(404)
    new_review = request.get_json()
    if not new_review:
        abort(400, "Not a JSON")
    if "user_id" not in new_review:
        abort(400, "Missing user_id")
    user_id = new_review['user_id']
    if not storage.get("User", user_id):
        abort(404)
    if "text" not in new_review:
        abort(400, "Missing text")
    review = Review(**new_review)
    setattr(review, 'place_id', place_id)
    storage.new(review)
    storage.save()
    return make_response(jsonify(review.to_dict()), 201)


@app_views.route('/api/v1/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Updates a specific Review object."""
    review = storage.get("Review", review_id)
    if not review:
        abort(404)

    body_request = request.get_json()
    if not body_request:
        abort(400, "Not a JSON")

    for k, v in body_request.items():
        if k not in ['id', 'user_id', 'place_id',
                     'created_at', 'updated_at']:
            setattr(review, k, v)
    
    storage.save()
    return jsonify(review.to_dict()), 200
