from src.core.inventory.models import InventoryItem
from sqlalchemy.orm import Session

class InventoryRepository:
    """
    InventoryRepository provides methods for interacting with the InventoryItem database table.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_items(self):
        """Fetch all inventory items from the database."""
        return self.db_session.query(InventoryItem).all()

    def get_item_by_id(self, item_id: int):
        """Fetch a single inventory item by its ID."""
        return self.db_session.query(InventoryItem).filter(InventoryItem.id == item_id).first()

    def add_item(self, item: InventoryItem):
        """Add a new inventory item to the database."""
        self.db_session.add(item)
        self.db_session.commit()
        return item

    def update_item(self, item_id: int, **kwargs):
        """Update an existing inventory item with new data."""
        item = self.get_item_by_id(item_id)
        if not item:
            return None
        for key, value in kwargs.items():
            if hasattr(item, key):
                setattr(item, key, value)
        self.db_session.commit()
        return item

    def delete_item(self, item_id: int):
        """Delete an inventory item by its ID."""
        item = self.get_item_by_id(item_id)
        if item:
            self.db_session.delete(item)
            self.db_session.commit()
            return True
        return False
