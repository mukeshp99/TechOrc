Token Refresh API
================

This API provides a token refresh mechanism using bearer tokens.

Getting Started
---------------

1. Clone the repository: `git clone https://github.com/mukeshp99/TechOrc.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py makemigrations` and `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

API Endpoints
-------------

* `POST /api/token/refresh/`: Refreshes the bearer token.

Request Headers
---------------

* `Authorization`: The bearer token to be refreshed.

Response
--------

* `token`: The new bearer token.

Error Handling
--------------

* `401 Unauthorized`: The bearer token is invalid or expired.
* `500 Internal Server Error`: An error occurred while processing the request.

License
-------

This project is licensed under the MIT License.
