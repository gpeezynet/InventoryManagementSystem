from src.core.transactions.repositories import TransactionRepository
from src.core.transactions.models import Transaction

class TransactionService:
    """
    TransactionService provides business logic for managing transactions.
    """

    def __init__(self, transaction_repository: TransactionRepository):
        self.transaction_repository = transaction_repository

    def get_all_transactions(self):
        """Fetch all transactions."""
        return self.transaction_repository.get_all_transactions()

    def get_transaction_by_id(self, transaction_id: int):
        """Fetch a transaction by its ID."""
        return self.transaction_repository.get_transaction_by_id(transaction_id)

    def create_transaction(self, item_id: int, quantity: int, timestamp):
        """Create and add a new transaction."""
        new_transaction = Transaction(item_id=item_id, quantity=quantity, timestamp=timestamp)
        return self.transaction_repository.add_transaction(new_transaction)

    def update_transaction(self, transaction_id: int, **kwargs):
        """Update an existing transaction."""
        return self.transaction_repository.update_transaction(transaction_id, **kwargs)

    def delete_transaction(self, transaction_id: int):
        """Delete a transaction by its ID."""
        return self.transaction_repository.delete_transaction(transaction_id)