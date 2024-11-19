from src.auth.models import User
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
    """
    AuthService provides methods for user authentication and management.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_user(self, username: str, password: str, email: str, full_name: str = None):
        """Create a new user with a hashed password."""
        if self.get_user_by_username(username):
            raise ValueError("Username already exists.")
        if self.get_user_by_email(email):
            raise ValueError("Email already exists.")
        
        password_hash = generate_password_hash(password)
        new_user = User(
            username=username,
            password_hash=password_hash,
            email=email,
            full_name=full_name
        )
        self.db_session.add(new_user)
        self.db_session.commit()
        return new_user

    def get_user_by_username(self, username: str):
        """Fetch a user by their username."""
        return self.db_session.query(User).filter(User.username == username).first()

    def get_user_by_email(self, email: str):
        """Fetch a user by their email."""
        return self.db_session.query(User).filter(User.email == email).first()

    def verify_user_password(self, username: str, password: str):
        """Verify a user's password."""
        user = self.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            return True
        return False

    def update_user_password(self, username: str, new_password: str):
        """Update the password for an existing user."""
        user = self.get_user_by_username(username)
        if not user:
            raise ValueError("User not found.")
        
        user.password_hash = generate_password_hash(new_password)
        self.db_session.commit()
        return user

    def delete_user(self, username: str):
        """Delete a user by their username."""
        user = self.get_user_by_username(username)
        if user:
            self.db_session.delete(user)
            self.db_session.commit()
            return True
        return False
