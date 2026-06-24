# Hands-On 04

## Topic

Flask — App Structure, Routing, Jinja2 & Blueprints

---

## Objective

To rebuild the Course Management backend using Flask, understand Flask application structure, define API routes using Blueprints, handle JSON requests and responses, and implement CRUD operations for courses.

---

## Tasks Completed

### Task 1 - Flask App Structure and Basic Routing

Created a new Flask project named `flask_coursemanager` with the following structure:

- `app.py` → application entry point
- `config.py` → configuration settings
- `courses/` package
  - `__init__.py`
  - `routes.py`

Implemented the Flask application using the **application factory pattern** with `create_app()`.

Configured the app using a `Config` class and loaded it into the Flask app.

Created and registered a Blueprint:

- `courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')`

Added basic API routes:

- `GET /api/courses/`
- `POST /api/courses/`

---

### Task 2 - Request Handling and JSON Responses

Extended the API to support full CRUD operations for courses.

Implemented the following endpoints:

- `GET /api/courses/`
- `POST /api/courses/`
- `GET /api/courses/<course_id>/`
- `PUT /api/courses/<course_id>/`
- `DELETE /api/courses/<course_id>/`

Used `request.get_json()` to parse incoming JSON request data.

Validated required fields:
- `name`
- `code`
- `credits`

Added a helper function `make_response_json()` to return a consistent JSON response structure.

Implemented JSON error responses for:
- `400 Bad Request`
- `404 Not Found`
- `500 Internal Server Error`

---

## Technologies Used

- Python
- Flask
- Flask Blueprints
- JSON API Routing

---

## Outcome

Successfully created a modular Flask backend for the Course Management System, implemented CRUD-style API routes using Blueprints, handled JSON request and response objects, validated request payloads, and returned structured API error responses.