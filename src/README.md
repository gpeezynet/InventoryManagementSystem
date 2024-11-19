# Inventory Management System

## Overview
The Inventory Management System is a comprehensive web-based application designed to streamline the management of inventory. Built using Python and Flask, it offers features such as inventory tracking, transaction logging, and reporting. The application is containerized using Docker for consistent deployment and is integrated with PostgreSQL as the database.

## Features
- **Inventory Management**: Add, update, and delete inventory items.
- **Transaction Tracking**: Record and view item transactions.
- **User Authentication**: Secure user registration and login.
- **Reporting**: Generate and export daily inventory reports.
- **CSV Import**: Parse and import data from CSV files for batch updates.

## Project Structure
```
inventory_system/
├── src/
│   ├── core/
│   │   ├── inventory/
│   │   ├── transactions/
│   │   └── reporting/
│   ├── api/
│   ├── auth/
│   └── utils/
├── tests/
├── config/
├── requirements.txt
├── docker-compose.yml
└── README.md
```

## Prerequisites
- Python 3.8+
- Docker & Docker Compose
- PostgreSQL (or use the provided Docker configuration)

## Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/inventory_management_system.git
   cd inventory_management_system
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root:
   ```env
   FLASK_APP=src/api/routes.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgresql://user:password@db:5432/inventory_db
   ```

5. **Run Database Migrations**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Start the Application with Docker**:
   ```bash
   docker-compose up --build
   ```

## Usage
- Access the application at `http://localhost:5000`
- Use the provided API routes to interact with the inventory and transaction services.

## Testing
Run tests using the following command:
```bash
python -m unittest discover -s tests
```

## Contributing
Contributions are welcome! Please create a branch, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

*Happy Managing!*
