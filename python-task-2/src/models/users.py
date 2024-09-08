from src.db.db_connector import db


class User(db.Model):
    """
    Represents a user in the database.

    Attributes:
        id (int): Unique identifier for the user, serves as the primary key.
        username (str): Username of the user, must be unique and cannot be null.
        password (str): Hashed password of the user, cannot be null.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
