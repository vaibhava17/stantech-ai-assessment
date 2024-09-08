import pymysql
from flask_sqlalchemy import SQLAlchemy

# Ensure pymysql is used as the MySQL client library.
# This allows SQLAlchemy to interact with MySQL databases through pymysql.
pymysql.install_as_MySQLdb()

# Create an instance of SQLAlchemy
# This instance will be used to manage database interactions and ORM mappings.
db = SQLAlchemy()


def create_connection(app):
    """
    Initialize the SQLAlchemy database connection with the Flask app.

    This function binds the SQLAlchemy instance to the Flask application, allowing
    the app to interact with the database. It sets up the database connection based
    on the configurations specified in the app's configuration.

    Args:
        app (Flask): The Flask application instance to initialize the database with.

    Returns:
        SQLAlchemy: The SQLAlchemy instance connected to the Flask app.
    """

    # Import the database models for User and Product
    # These models define the structure of the `users` and `products` tables in the database.
    from src.models.users import User
    from src.models.products import Product

    db.init_app(app)

    # This ensures that the `users` and `products` tables are created in the database if they don't exist.
    with app.app_context():
        db.create_all()

    return db
