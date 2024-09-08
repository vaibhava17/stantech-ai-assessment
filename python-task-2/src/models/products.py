from src.db.db_connector import db


class Product(db.Model):
    """
    Represents a product in the database.

    Attributes:
        product_id (int): Unique identifier for the product.
        product_name (str): Name of the product.
        category (str): Category to which the product belongs.
        price (float): Price of the product.
        quantity_sold (int): Quantity of the product sold.
        rating (float): Average rating of the product.
        review_count (int): Number of reviews for the product.
    """

    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    price = db.Column(db.Float)
    quantity_sold = db.Column(db.Integer)
    rating = db.Column(db.Float)
    review_count = db.Column(db.Integer)
