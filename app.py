
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)
api = Api(app)

class ItemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"Item(name = {name}, description = {description})"

db.create_all()

class ItemResource(Resource):
    def get(self, item_id):
        item = ItemModel.query.filter_by(id=item_id).first()
        if item:
            return {"id": item.id, "name": item.name, "description": item.description}, 200
        return {"error": "Item not found"}, 404

    def post(self):
        item_data = request.get_json()
        new_item = ItemModel(name=item_data["name"], description=item_data.get("description"))
        db.session.add(new_item)
        db.session.commit()
        return {"message": "Item created successfully."}, 201

    def put(self, item_id):
        item_data = request.get_json()
        item = ItemModel.query.filter_by(id=item_id).first()
        if item:
            item.name = item_data["name"]
            item.description = item_data.get("description")
            db.session.commit()
            return {"message": "Item updated successfully."}, 200
        return {"error": "Item not found"}, 404

    def patch(self, item_id):
        item_data = request.get_json()
        item = ItemModel.query.filter_by(id=item_id).first()
        if item:
            item.name = item_data.get("name", item.name)
            item.description = item_data.get("description", item.description)
            db.session.commit()
            return {"message": "Item updated successfully."}, 200
        return {"error": "Item not found"}, 404

    def delete(self, item_id):
        item = ItemModel.query.filter_by(id=item_id).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return {"message": "Item deleted successfully."}, 200
        return {"error": "Item not found"}, 404

api.add_resource(ItemResource, "/item/<int:item_id>", "/item")

if __name__ == "__main__":
    app.run(debug=True)
