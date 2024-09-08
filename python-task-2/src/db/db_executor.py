from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.db.db_connector import db


class DBExecutor:
    """
    A class to execute SQL queries against the database using SQLAlchemy.

    This class provides methods to execute various types of SQL queries, including
    SELECT, INSERT, UPDATE, and DELETE. It manages database connections and handles
    errors that may arise during query execution.
    """

    @staticmethod
    def execute_query(query, params=None):
        """
        Execute a given SQL query with optional parameters.

        This method checks if the database engine is initialized, executes the provided
        SQL query, and commits the transaction if the query is an INSERT, UPDATE, or DELETE.

        Args:
            query (str): The SQL query to be executed.
            params (dict, optional): A dictionary of parameters to be used in the query.

        Returns:
            list: The results of the query if it is a SELECT statement, or a success message
                   if it is an INSERT, UPDATE, or DELETE statement.

        Raises:
            Exception: If the database engine is not initialized or if an error occurs during
                       query execution.
        """
        # Check if the database engine has been initialized
        if db.engine is None:
            raise Exception("Database engine is not initialized.")

        try:
            # Establish a connection to the database
            with db.engine.connect() as connection:
                # Execute the query with the provided parameters
                result = connection.execute(text(query), params or {})

                # If the query is an INSERT, UPDATE, or DELETE, commit the transaction
                if query.strip().lower().startswith(('insert', 'update', 'delete')):
                    connection.commit()
                    return "Query executed successfully."

                # For SELECT queries, return the fetched results
                return result.fetchall()

        except SQLAlchemyError as e:
            # Handle SQLAlchemy errors by printing the error message and returning None
            print(f"An error occurred: {str(e)}")
            return None
