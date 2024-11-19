# src/core/transactions/models.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from config.database import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    inventory_item_id = Column(Integer, ForeignKey('inventory_items.id'))
    quantity = Column(Integer)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"<Transaction(item_id='{self.inventory_item_id}', quantity='{self.quantity}')>"
