from flask import request, Blueprint
from models import db, Item

bp = Blueprint('items', __name__, url_prefix='/item')

@bp.route('/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    if item is None:
        return {"error": "not found"}, 404
    return {"name": item.name}

@bp.route('', methods=['POST'])
def create_item():
    name = request.json.get('name')
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return {"id": item.id}

@bp.route('/<id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get(id)
    if item is None:
        return {"error": "not found"}, 404
    item.name = request.json.get('name')
    db.session.commit()
    return {"success": True}

@bp.route('/<id>', methods=['PATCH'])
def partial_update_item(id):
    item = Item.query.get(id)
    if item is None:
        return {"error": "not found"}, 404
    if 'name' in request.json:
        item.name = request.json.get('name')
    db.session.commit()
    return {"success": True}

@bp.route('/<id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if item is None:
        return {"error": "not found"}, 404
    db.session.delete(item)
    db.session.commit()
    return {"success": True}

