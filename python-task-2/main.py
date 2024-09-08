from flask import Flask
from flask_jwt_extended import JWTManager

from src.db.db_connector import db, create_connection
from src.db.db_initializer import DatabaseInitializer
from src.config import config
from src.routes import routes

# Initialize the Flask app
app = Flask(__name__)

# Load the application configuration from the config module
app.config.from_object(config)

# Initialize JWTManager to handle authentication and token management
jwt = JWTManager(app)

# The DatabaseInitializer checks if the database exists, and creates it if not
db_initializer = DatabaseInitializer(
    host=config.MYSQL_HOST,
    user=config.MYSQL_USER,
    password=config.MYSQL_PASSWORD,
    database_name=config.MYSQL_DATABASE_NAME
)
db_initializer.initialize()

# Establish the database connection by creating the connection within the app context
create_connection(app)

# Initialize the API routes by attaching them to the Flask app
api = routes.API(app)

# Entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
