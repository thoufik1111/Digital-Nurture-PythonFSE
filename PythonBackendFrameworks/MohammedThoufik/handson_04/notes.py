"""
HANDS-ON 04
Flask - App Structure, Routing, Jinja2 & Blueprints

=================================================
1. FLASK FRAMEWORK
=================================================

Flask is a lightweight Python web framework used
to build web applications and APIs.

Unlike Django, Flask is minimal and gives the
developer more control over project structure.

Flask is commonly used for:
- REST APIs
- lightweight backend services
- microservices
- quick prototypes


=================================================
2. FLASK APPLICATION STRUCTURE
=================================================

In this hands-on, a separate Flask project was created
for the Course Management System.

Project structure:

flask_coursemanager/
│
├── app.py
├── config.py
└── courses/
    ├── __init__.py
    └── routes.py

Purpose of each file:

app.py
- Entry point of the Flask application
- Creates the app using create_app()
- Registers blueprints
- Adds error handlers

config.py
- Stores configuration settings such as
  SECRET_KEY, DEBUG and database URI

courses/routes.py
- Contains all API routes related to courses


=================================================
3. APPLICATION FACTORY PATTERN
=================================================

The application factory pattern means the Flask app
is created inside a function, usually create_app().

Example:
def create_app():
    app = Flask(__name__)
    return app

Benefits:
- Better project structure
- Easier testing
- Avoids circular import issues
- More scalable for larger applications


=================================================
4. BLUEPRINTS
=================================================

Blueprints are Flask's way of organizing routes
into separate modules.

In this hands-on, a blueprint was created for course routes:

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses')

This means all course-related endpoints start with:
/api/courses/

Benefits of Blueprints:
- Keeps code modular
- Makes the app cleaner
- Helps separate different features into different files


=================================================
5. ROUTING IN FLASK
=================================================

Routes define which function should run when a
specific URL is requested.

Routes created in this hands-on:

GET    /api/courses/
POST   /api/courses/
GET    /api/courses/<course_id>/
PUT    /api/courses/<course_id>/
DELETE /api/courses/<course_id>/

These routes simulate CRUD operations for courses.


=================================================
6. REQUEST AND RESPONSE OBJECTS
=================================================

Flask uses the request object to read incoming
client data.

request.get_json()
- Reads JSON data sent in POST or PUT requests

jsonify(...)
- Converts Python dictionaries/lists into JSON response

In this hands-on, request.get_json() was used to
receive course data such as:
- name
- code
- credits


=================================================
7. JSON RESPONSE HANDLING
=================================================

A helper function make_response_json() was created
to return a consistent API response format.

Example response structure:
{
    "status": "success",
    "data": {...}
}

Error responses were also handled using JSON so that
the API never returns HTML pages for errors.


=================================================
8. ERROR HANDLING
=================================================

Flask error handlers were added for:
- 404 Not Found
- 500 Internal Server Error

This ensures the backend always returns JSON responses
even when a route does not exist or an internal error occurs.


=================================================
9. LEARNINGS
=================================================

- Created a modular Flask application
- Used the application factory pattern
- Defined and registered Blueprints
- Implemented GET, POST, PUT and DELETE routes
- Parsed request JSON using request.get_json()
- Validated required fields in API requests
- Returned structured JSON responses
- Added JSON error handlers for API consistency
"""