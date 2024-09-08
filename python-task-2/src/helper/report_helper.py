import pandas as pd

from src.db.db_executor import DBExecutor
from src.config import config
from src.queries import queries


class ReportHelper:
    """
    A helper class for generating reports based on product data from the database.

    Attributes:
        df (pd.DataFrame): DataFrame containing product data fetched from the database.
    """

    def __init__(self):
        """
        Initialize the ReportHelper and fetch data from the database to populate the DataFrame.
        """
        self.df = self.fetch_data()

    @staticmethod
    def fetch_data():
        """
        Fetch product data from the database and load it into a DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing product data.

        Raises:
            Exception: If data fetching fails or results in None.
        """
        query = queries.GET_ALL_PRODUCTS
        result = DBExecutor().execute_query(query)

        if result is None:
            raise Exception("Failed to fetch data from the database.")

        # Create DataFrame from the fetched data
        df = pd.DataFrame(result, columns=config.COLUMNS_FOR_DATAFRAME)
        return df

    def generate_summary(self):
        """
        Generate a summary report of the product data, including total revenue and top-selling products
        for each category. The result is converted to an HTML table format.

        Returns:
            str: HTML table representation of the summary report.
        """
        # Convert columns to numeric, coercing errors to NaN
        self.df['price'] = pd.to_numeric(self.df['price'], errors='coerce')
        self.df['quantity_sold'] = pd.to_numeric(self.df['quantity_sold'], errors='coerce')

        # Calculate total revenue for each product
        self.df['total_revenue'] = self.df['price'] * self.df['quantity_sold']

        # Aggregate data to get total revenue per category
        summary_df = self.df.groupby('category').agg(
            total_revenue=('total_revenue', 'sum')
        ).reset_index()

        # Identify the top-selling product in each category
        top_products = self.df.loc[
            self.df.groupby('category')['quantity_sold'].idxmax()
        ].reset_index(drop=True)

        # Merge top-selling products with the summary DataFrame
        summary_df = summary_df.merge(
            top_products[['category', 'product_name', 'quantity_sold']],
            on='category',
            how='left'
        )

        # Rename columns for clarity
        summary_df.rename(columns={
            'product_name': 'top_product',
            'quantity_sold': 'top_product_quantity_sold'
        }, inplace=True)

        # Sort the summary DataFrame by total revenue in descending order
        summary_df.sort_values(by='total_revenue', ascending=False, inplace=True)

        # Convert the summary DataFrame to an HTML table
        html_table = summary_df.to_html(classes='table table-striped', index=False)

        return html_table
