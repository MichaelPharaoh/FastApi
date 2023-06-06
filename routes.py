from flask import Blueprint, request, jsonify
from .models import Item
from . import db

bp = Blueprint('bp', __name__)

@bp.route('/', methods=['GET'])
def home():
    return "Welcome to my application!"

@bp.route('/items/', methods=['GET'], strict_slashes=False)
def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@bp.route('/items/<int:id>', methods=['GET'], strict_slashes=False)
def get_item(id):
    item = Item.query.get(id)
    if item is None:
        return {'error': 'not found'}, 404
    return item.to_dict()

@bp.route('/items/', methods=['POST'], strict_slashes=False)
def create_item():
    data = request.get_json() or {}
    item = Item()
    item.from_dict(data)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@bp.route('/items/<int:id>', methods=['PUT'], strict_slashes=False)
def update_item(id):
    item = Item.query.get(id)
    if item is None:
        return {'error': 'not found'}, 404
    data = request.get_json() or {}
    item.from_dict(data)
    db.session.commit()
    return jsonify(item.to_dict())

@bp.route('/items/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_item(id):
    item = Item.query.get(id)
    if item is None:
        return {'error': 'not found'}, 404
    db.session.delete(item)
    db.session.commit()
    return '', 204

