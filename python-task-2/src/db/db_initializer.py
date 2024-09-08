import pymysql
from pymysql.cursors import DictCursor


class DatabaseInitializer:
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name

    def create_database_if_not_exists(self):
        # Create the database if it does not already exist.
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            cursorclass=DictCursor
        )

        try:
            with connection.cursor() as cursor:
                # Check if the database exists
                cursor.execute(f"SHOW DATABASES LIKE '{self.database_name}'")
                result = cursor.fetchone()

                if result is None:
                    # Create the database if it does not exist
                    cursor.execute(f"CREATE DATABASE {self.database_name}")
                    print(f"Database '{self.database_name}' created successfully.")
                else:
                    print(f"Database '{self.database_name}' already exists.")

                # Optionally, select the database to work with
                connection.select_db(self.database_name)

        finally:
            connection.close()

    def initialize(self):
        # Initialize the database creation process.
        self.create_database_if_not_exists()
