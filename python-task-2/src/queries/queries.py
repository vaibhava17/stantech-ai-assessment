# SQL query strings for interacting with the database

INSERT_PRODUCT = (
    "INSERT INTO products (product_name, category, price, quantity_sold, rating, review_count) "
    "VALUES (:product_name, :category, :price, :quantity_sold, :rating, :review_count)"
)

GET_ALL_PRODUCTS = "SELECT * FROM products"

INSERT_USER = "INSERT INTO users (username, password) VALUES (:username, :password)"

GET_USER_BY_USERNAME = "SELECT * FROM users WHERE username = :username"
