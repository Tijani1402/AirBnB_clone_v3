#!/usr/bin/python3
<<<<<<< HEAD
"""View to handle all amenites objects"""

from models import storage
from api.v1.views import app_views
from models.base_model import BaseModel
from flask import jsonify, abort, request, make_response
=======
"""states.py"""

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
>>>>>>> aysuarex
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
<<<<<<< HEAD
def all_amenities():
    """Return all amenities objects"""
    amenities = storage.all(Amenity)
    amenitiess = []
    for amen in amenities.values():
        amenitiess.append(amen.to_dict())
    return jsonify(amenitiess)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def one_amenity(amenity_id):
    """Get a single amenity"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
=======
def get_amenities():
    """get amenity information for all amenities"""
    amenities = []
    for amenity in storage.all("Amenity").values():
        amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity(amenity_id):
    """get amenity information for specified amenity"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
>>>>>>> aysuarex
        abort(404)
    return jsonify(amenity.to_dict())


<<<<<<< HEAD
@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_amenity(amenity_id):
    """Delete an amenity obj with its id"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    amenity.delete()
    storage.save()
    return make_response({}, 200)
=======
@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """deletes an amenity based on its amenity_id"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return (jsonify({}))
>>>>>>> aysuarex


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
<<<<<<< HEAD
    """Post new amenity object"""
    post_req = request.get_json()
    if not post_req:
        abort(400, "Not a JSON")
    if 'name' not in post_req:
        abort(400, "Missing name")

    new_amen = Amenity(**post_req)
    storage.new(new_amen)
    storage.save()
    return make_response(new_amen.to_dict(), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """Update the amenity object with the provided id"""
    put_req = request.get_json()
    if not put_req:
        abort(400, "Not a JSON")
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    ignore_keys = ['id', 'created_id', 'updated_at']

    for key, value in put_req.items():
        if key not in ignore_keys:
            setattr(amenity, key, value)
    storage.save()
    return make_response(amenity.to_dict(), 200)
=======
    """create a new amenity"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    amenity = Amenity(**request.get_json())
    amenity.save()
    return make_response(jsonify(amenity.to_dict()), 201)


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenity(amenity_id):
    """update an amenity"""
    amenity = storage.get("Amenity", amenity_id)
    if amenity is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, attr, val)
    amenity.save()
    return jsonify(amenity.to_dict())
>>>>>>> aysuarex
