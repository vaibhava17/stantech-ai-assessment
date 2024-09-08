# Task 2

This is a Flask-based e-commerce application that includes user authentication, CSV data upload and processing, and a summary report generation. The app uses SQLAlchemy for ORM and integrates with various helper classes to manage uploads, authentication, and reporting.

## Features

- **User Authentication**: Sign up and login with JWT-based authentication.
- **CSV Data Upload**: Upload product data from CSV files and process it.
- **Data Cleaning**: Clean and normalize data before uploading.
- **Summary Report**: Generate a summary report of product sales and display it as an HTML table.

## Requirements

- Python 3.8+
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Pandas
- PyMySQL

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/vaibhava17/stantech-ai-assessment.git
    cd stantech-ai-assessment/python-task-2
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Go to `src/config/config.py` file and update the following:

    ```env
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=mysql://username:password@localhost/schema_name
    MYSQL_DATABASE_NAME = 'schema_name'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'username'
    MYSQL_PASSWORD = 'password'
    ```

## Running the Application

To run the Flask application in development mode:

```bash
python3 run
```

## Endpoints

- **`GET /`**: Test connection endpoint.
- **`POST /upload_csv`**: Upload a CSV file to add product data.
    - Requires a file upload with key `file`.
- **`POST /signup`**: Sign up a new user.
    - JSON body with `username` and `password`.
- **`GET /login`**: Log in an existing user.
    - JSON body with `username` and `password`.
- **`POST /clean_n_upload_csv`**: Upload and clean CSV data before adding to the database.
    - Requires a file upload with key `file`.
- **`GET /summary_report`**: Generate and return a summary report as an HTML table.

## Testing

To test the API endpoints, you can use tools like Postman or curl.

### Testing with Postman

Import postman collection from  `postman` folder and add files for upload_csv, clean_n_upload_csv from the directory

1. **Test Connection**
    - Method: `GET`
    - URL: `http://localhost:5000/`

2. **Upload CSV**
    - Method: `POST`
    - URL: `http://localhost:5000/upload_csv`
    - Body: Form-data, key: `file`, type: File.

3. **Sign Up**
    - Method: `POST`
    - URL: `http://localhost:5000/signup`
    - Body: JSON
      ```json
      {
        "username": "testuser",
        "password": "testpassword"
      }
      ```

4. **Login**
    - Method: `GET`
    - URL: `http://localhost:5000/login`
    - Body: JSON
      ```json
      {
        "username": "testuser",
        "password": "testpassword"
      }
      ```

5. **Clean and Upload CSV**
    - Method: `POST`
    - URL: `http://localhost:5000/clean_n_upload_csv`
    - Body: Form-data, key: `file`, type: File.

6. **Summary Report**
    - Method: `GET`
    - URL: `http://localhost:5000/summary_report`
