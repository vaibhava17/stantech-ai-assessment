# Configuration settings for the Flask application

# Secret key for signing cookies and JWT tokens.
# This should be kept secure and not hard-coded in production.
SECRET_KEY = 'your_secret_key'

# URI for connecting to the MySQL database.
# Format: 'mysql://username:password@hostname/database_name'
# Example: 'mysql://root:root@localhost/ecommerce_db'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/ecommerce_db'

# Disable SQLAlchemy event system that tracks modifications of objects.
# This can be set to 'False' to save resources and avoid overhead.
SQLALCHEMY_TRACK_MODIFICATIONS = False

# List of columns to be included in the DataFrame.
# This ensures only the specified columns are processed.
COLUMNS_FOR_DATAFRAME = [
    'product_id',         # Unique identifier for the product
    'product_name',       # Name of the product
    'category',           # Category to which the product belongs
    'price',              # Price of the product
    'quantity_sold',      # Quantity of the product sold
    'rating',             # Rating of the product
    'review_count'        # Number of reviews for the product
]

# MySQL Config
MYSQL_DATABASE_NAME = 'ecommerce_db' # Database Name
MYSQL_HOST = 'localhost' # Hostname
MYSQL_USER = 'root' # Username
MYSQL_PASSWORD = 'root' # Password
