from flask import Flask, jsonify, request
from src.core.inventory.services import InventoryService
from src.core.inventory.models import InventoryItem
from src.core.inventory.repositories import InventoryRepository
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Database setup (replace 'sqlite:///your_database.db' with your actual DB URI)
engine = create_engine('sqlite:///your_database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Initialize the service with the repository
inventory_repository = InventoryRepository(session)
inventory_service = InventoryService(inventory_repository)

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    """Endpoint to get all inventory items."""
    inventory_items = inventory_service.get_all_items()
    return jsonify([{
        'id': item.id,
        'name': item.name,
        'quantity': item.quantity
    } for item in inventory_items]), 200

@app.route('/inventory', methods=['POST'])
def add_inventory_item():
    """Endpoint to add a new inventory item."""
    data = request.get_json()
    if not data or 'name' not in data or 'quantity' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    new_item = InventoryItem(name=data['name'], quantity=data['quantity'])
    created_item = inventory_service.create_item(new_item)
    return jsonify({
        'id': created_item.id,
        'name': created_item.name,
        'quantity': created_item.quantity
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
