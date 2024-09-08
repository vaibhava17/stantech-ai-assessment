from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from src.db.db_executor import DBExecutor
from src.queries import queries


class AuthHelper:
    """
    A helper class for handling user authentication tasks, including user registration
    and login. This class interacts with the database to manage user data and generate
    authentication tokens.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
        access_token (str): The JWT access token for authenticated users.
    """

    def __init__(self, username, password):
        """
        Initialize the AuthHelper with a username and password.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.username = username
        self.password = password
        self.access_token = None

    def get_user(self):
        """
        Retrieve user information from the database based on the username.

        Returns:
            dict: A dictionary containing user information (user_id, username, and password)
                  if the user exists, otherwise None.

        Raises:
            Exception: If the username or password is missing, or if an error occurs while
                       retrieving user data from the database.
        """
        user = None
        try:
            if self.username is None or self.password is None:
                raise Exception("Username and password are required")

            query = queries.GET_USER_BY_USERNAME
            params = {'username': self.username}

            result = DBExecutor.execute_query(query, params)

            for row in result:
                user = {
                    'user_id': row[0],
                    'username': row[1],
                    'password': row[2],
                }
            return user
        except Exception as e:
            raise Exception(f"Error getting user: {e}")

    def signup_user(self):
        """
        Register a new user by storing their username and hashed password in the database.

        Raises:
            Exception: If the username or password is missing, if the username already exists,
                       or if an error occurs while creating the user in the database.
        """
        try:
            if self.username is None or self.password is None:
                raise Exception("Username and password are required")

            user_exist = self.get_user()

            if user_exist:
                raise Exception("Username is already taken")

            # Hash the password before storing it
            hashed_password = generate_password_hash(self.password, method='pbkdf2:sha256')

            query = queries.INSERT_USER
            params = {
                'username': self.username,
                'password': hashed_password
            }
            DBExecutor.execute_query(query, params)
        except Exception as e:
            raise Exception(f"Error creating user: {e}")

    def login_user(self):
        """
        Authenticate a user by verifying their username and password, and generate a JWT token.

        Returns:
            str: The JWT access token for the authenticated user.

        Raises:
            Exception: If the username or password is missing, if the credentials are invalid,
                       or if an error occurs while authenticating the user.
        """
        try:
            if self.username is None or self.password is None:
                raise Exception("Username and password are required")

            user = self.get_user()

            if not user or not check_password_hash(user['password'], self.password):
                raise Exception("Invalid username or password")

            # Generate JWT access token
            access_token = create_access_token(identity={'username': user['username']})
            return access_token
        except Exception as e:
            raise Exception(f"Error getting user: {e}")
