import pandas as pd
from flask import current_app

from src.db.db_executor import DBExecutor
from src.queries import queries


class UploadHelper:
    """
    A helper class for handling the upload of product data from a CSV file to the database.

    Attributes:
        file (file): CSV file containing product data.
        df (pd.DataFrame): DataFrame for holding CSV data.
    """

    def __init__(self, file):
        """
        Initialize the UploadHelper with the path to the CSV file.

        Args:
            file (file): Path to the CSV file.
        """
        self.file = file
        self.df = None

    def load_csv_to_dataframe(self):
        """
        Load CSV data from the file into a DataFrame.

        Raises:
            Exception: If the file is not found or if there is an error loading the CSV data.
        """
        try:
            self.df = pd.read_csv(self.file)
        except FileNotFoundError:
            raise Exception(f"File not found at path: {self.file}")
        except Exception as e:
            raise Exception(f"Error loading CSV: {e}")

    def upload_data_to_db(self):
        """
        Upload the data from the DataFrame to the database.

        Raises:
            Exception: If the DataFrame is empty or if there is an error during the upload process.
        """
        try:
            if self.df is None:
                raise Exception("DataFrame is empty. Load CSV data first.")

            query = queries.INSERT_PRODUCT

            for index, row in self.df.iterrows():
                params = {
                    'product_name': row['product_name'],
                    'category': row['category'],
                    'price': row['price'],
                    'quantity_sold': row['quantity_sold'],
                    'rating': row['rating'],
                    'review_count': row['review_count']
                }
                DBExecutor.execute_query(query, params)
        except Exception as e:
            raise Exception(f"Error uploading data to database: {e}")

    def load_n_upload_data(self):
        """
        Load CSV data into a DataFrame and upload it to the database within the Flask app context.
        """
        with current_app.app_context():
            self.load_csv_to_dataframe()
            self.upload_data_to_db()

    def clean_data(self):
        """
        Clean and preprocess the DataFrame:
            - Convert columns to numeric values, coercing errors to NaN.
            - Fill missing values in price, quantity_sold, and review_count with their respective medians.
            - Fill missing rating values with the average rating per category.
        """
        self.df['price'] = pd.to_numeric(self.df['price'], errors='coerce')
        self.df['quantity_sold'] = pd.to_numeric(self.df['quantity_sold'], errors='coerce')
        self.df['rating'] = pd.to_numeric(self.df['rating'], errors='coerce')
        self.df['review_count'] = pd.to_numeric(self.df['review_count'], errors='coerce')

        # Calculate medians
        price_median = self.df['price'].median()
        quantity_median = self.df['quantity_sold'].median()
        review_count_median = self.df['review_count'].median()

        # Fill missing values with medians
        self.df['price'].fillna(price_median, inplace=True)
        self.df['quantity_sold'].fillna(quantity_median, inplace=True)
        self.df['review_count'].fillna(review_count_median, inplace=True)

        # Fill missing rating values with average rating per category
        avg_rating_per_category = self.df.groupby('category')['rating'].transform('mean')
        self.df['rating'] = self.df['rating'].fillna(avg_rating_per_category)

    def load_clean_n_upload_data(self):
        """
        Load CSV data into a DataFrame, clean the data, and upload it to the database.
        """
        self.load_csv_to_dataframe()
        self.clean_data()
        self.upload_data_to_db()
