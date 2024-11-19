from src.core.transactions.models import Transaction
from sqlalchemy.orm import Session

class TransactionRepository:
    """
    TransactionRepository provides methods for interacting with the Transaction database table.
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_all_transactions(self):
        """Fetch all transactions from the database."""
        return self.db_session.query(Transaction).all()

    def get_transaction_by_id(self, transaction_id: int):
        """Fetch a single transaction by its ID."""
        return self.db_session.query(Transaction).filter(Transaction.id == transaction_id).first()

    def add_transaction(self, transaction: Transaction):
        """Add a new transaction to the database."""
        self.db_session.add(transaction)
        self.db_session.commit()
        return transaction

    def update_transaction(self, transaction_id: int, **kwargs):
        """Update an existing transaction with new data."""
        transaction = self.get_transaction_by_id(transaction_id)
        if not transaction:
            return None
        for key, value in kwargs.items():
            if hasattr(transaction, key):
                setattr(transaction, key, value)
        self.db_session.commit()
        return transaction

    def delete_transaction(self, transaction_id: int):
        """Delete a transaction by its ID."""
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            self.db_session.delete(transaction)
            self.db_session.commit()
            return True
        return False
