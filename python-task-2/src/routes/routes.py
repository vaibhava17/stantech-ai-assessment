from flask import request, jsonify, render_template_string

from src.helper.upload_helper import UploadHelper
from src.helper.report_helper import ReportHelper
from src.helper.auth_helper import AuthHelper


class API:
    def __init__(self, app=None):
        """
        Initialize the API class and add routes if an app instance is provided.

        :param app: Flask application instance
        """
        if app is not None:
            self.add_routes(app)

    @staticmethod
    def add_routes(app):
        """
        Define and add routes to the Flask application.

        :param app: Flask application instance
        """
        @app.route('/', methods=['GET'])
        def test_connection():
            """
            Test route to check if the server is up and running.

            :return: JSON response indicating success or failure
            """
            try:
                return jsonify({"message": "Connection Successful."}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route('/upload_csv', methods=['POST'])
        def upload_csv():
            """
            Upload a CSV file and process its data.

            - Checks for file presence in request.
            - Uses UploadHelper to load and upload data to the database.

            :return: JSON response indicating success or error
            """
            try:
                if 'file' not in request.files:
                    return jsonify({"error": "No file part in the request"}), 400

                file = request.files['file']

                if file.filename == '':
                    return jsonify({"error": "No file selected"}), 400

                uploader_helper_obj = UploadHelper(file)
                uploader_helper_obj.load_n_upload_data()

                return jsonify({"message": "Data uploaded successfully."}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 400

        @app.route('/signup', methods=['POST'])
        def signup():
            """
            Register a new user.

            - Extracts username and password from request JSON.
            - Uses AuthHelper to create a new user.

            :return: JSON response indicating success or error
            """
            try:
                data = request.get_json()
                username = data.get('username')
                password = data.get('password')

                if not username or not password:
                    return jsonify({"error": "Username and password are required"}), 400

                auth_helper_obj = AuthHelper(username, password)
                auth_helper_obj.signup_user()

                return jsonify({"message": "User created successfully"}), 201

            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route('/login', methods=['GET'])
        def login():
            """
            Authenticate a user and generate an access token.

            - Extracts username and password from request JSON.
            - Uses AuthHelper to authenticate the user and generate a token.

            :return: JSON response containing access token or error
            """
            try:
                data = request.get_json()
                username = data.get('username')
                password = data.get('password')

                if not username or not password:
                    return jsonify({"error": "Username and password are required"}), 400

                auth_helper_obj = AuthHelper(username, password)
                access_token = auth_helper_obj.login_user()

                return jsonify({"access_token": access_token}), 200

            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route('/clean_n_upload_csv', methods=['POST'])
        def clean_n_upload_csv():
            """
            Upload a CSV file, clean the data, and upload it to the database.

            - Checks for file presence in request.
            - Uses UploadHelper to load, clean, and upload data.

            :return: JSON response indicating success or error
            """
            try:
                if 'file' not in request.files:
                    return jsonify({"error": "No file part in the request"}), 400

                file = request.files['file']

                if file.filename == '':
                    return jsonify({"error": "No file selected"}), 400

                uploader_helper_obj = UploadHelper(file)
                uploader_helper_obj.load_clean_n_upload_data()

                return jsonify({"message": "Data cleaning completed and uploaded successfully."}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        @app.route('/summary_report', methods=['GET'])
        def summary_report():
            """
            Generate and return a summary report in HTML format.

            - Uses ReportHelper to generate a summary report.
            - Renders the report as an HTML table.

            :return: HTML response containing the summary report or error
            """
            try:
                report_helper_obj = ReportHelper()
                html_table = report_helper_obj.generate_summary()

                html_content = f"""
                        <html>
                        <head>
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
                            <style>
                                table {{ 
                                    width: 100%;
                                }}
                                tr {{
                                    text-align: center !important;
                                }}
                            </style>
                        </head>
                        <body>
                            <div class="container">
                                <h2>Summary Report</h2>
                                {html_table}
                            </div>
                        </body>
                        </html>
                        """

                return render_template_string(html_content)
            except Exception as e:
                return f"An error occurred: {str(e)}", 500
