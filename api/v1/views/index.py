#!/usr/bin/python3
<<<<<<< HEAD
"""
return status of the page
"""

from flask import jsonify
from api.v1.views import app_views
=======
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
>>>>>>> aysuarex
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


<<<<<<< HEAD
@app_views.route('/status', methods=['GET'])
def get_status():
    """Retrive response status"""
    return jsonify({
        'status': 'OK'
    })


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """retrieves the number of each objects by type"""

    return jsonify({
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    })
=======
hbnbText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """hbnbStats"""
    return_dict = {}
    for key, value in hbnbText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)

if __name__ == "__main__":
    pass
>>>>>>> aysuarex
