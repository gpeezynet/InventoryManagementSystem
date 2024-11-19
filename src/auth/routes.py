from flask import Blueprint, request, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.auth.services import AuthService
from src.auth.models import User

# Create a new Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

# Database setup (replace 'sqlite:///your_database.db' with your actual DB URI)
engine = create_engine('sqlite:///your_database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Initialize the AuthService
auth_service = AuthService(session)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new user."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    try:
        new_user = auth_service.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            full_name=data.get('full_name')
        )
        return jsonify({
            'id': new_user.id,
            'username': new_user.username,
            'email': new_user.email
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    """Endpoint to authenticate a user."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    if auth_service.verify_user_password(data['username'], data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@auth_bp.route('/change-password', methods=['PUT'])
def change_password():
    """Endpoint to change the password of an existing user."""
    data = request.get_json()
    if not data or 'username' not in data or 'new_password' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    try:
        updated_user = auth_service.update_user_password(
            username=data['username'],
            new_password=data['new_password']
        )
        return jsonify({'message': 'Password updated successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/delete-user', methods=['DELETE'])
def delete_user():
    """Endpoint to delete a user."""
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    if auth_service.delete_user(data['username']):
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404