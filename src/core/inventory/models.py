# src/core/inventory/models.py
from sqlalchemy import Column, Integer, String
from config.database import Base

class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)

    def __repr__(self):
        return f"<InventoryItem(name='{self.name}', quantity='{self.quantity}')>"
