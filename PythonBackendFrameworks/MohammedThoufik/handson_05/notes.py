"""
HANDS-ON 05
Flask with SQLAlchemy ORM & Database Integration

=================================================
1. FLASK-SQLALCHEMY
=================================================

Flask-SQLAlchemy is an ORM extension for Flask that
simplifies database interaction using Python classes
instead of writing raw SQL queries.

It allows us to:
- define database tables as Python models
- perform CRUD operations using objects
- manage relationships between tables
- integrate easily with Flask applications


=================================================
2. ORM (OBJECT RELATIONAL MAPPING)
=================================================

ORM stands for Object Relational Mapping.

It maps:
- Python classes  -> Database tables
- Python objects  -> Table rows
- Class attributes -> Table columns

Example:
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

This creates a Course table with columns id and name.

Benefits of ORM:
- less manual SQL
- cleaner code
- easier maintenance
- object-based database interaction


=================================================
3. SQLALCHEMY MODEL DEFINITION
=================================================

In this hands-on, the following models were created:

- Department
- Course
- Student
- Enrollment

These models mirror the same Course Management schema
used in the earlier Django hands-ons.

Each model extends:
db.Model

Each model contains:
- table columns
- constraints
- foreign keys
- relationships
- to_dict() method for JSON conversion


=================================================
4. MODEL RELATIONSHIPS
=================================================

Relationships were added between models to represent
real-world associations in the Course Management system.

Examples:

Department
  ├── Courses
  └── Students

Student
  └── Enrollments

Course
  └── Enrollments

Enrollment acts as a bridge between Student and Course.

SQLAlchemy relationships used:
- db.relationship(...)
- db.ForeignKey(...)

These relationships allow easy navigation between
related records in Python code.


=================================================
5. FLASK-MIGRATE
=================================================

Flask-Migrate is used to manage database schema changes.

It works with Alembic internally and helps create
and apply migration scripts.

Commands used:

flask db init
- Initializes the migrations folder

flask db migrate -m "initial schema"
- Generates migration scripts based on model changes

flask db upgrade
- Applies migrations to the database

This allows the database schema to evolve without
manually recreating tables.


=================================================
6. DATABASE CRUD OPERATIONS
=================================================

In Hands-On 04, course data was stored in a Python list.
In Hands-On 05, that in-memory data was replaced with
real database operations using SQLAlchemy.

Examples used:
- Course.query.all()
- Course.query.get(course_id)
- db.session.add(new_course)
- db.session.delete(course)
- db.session.commit()

This means all API operations now read from and write
to the database instead of temporary Python variables.


=================================================
7. SERIALIZING ORM OBJECTS
=================================================

Flask does not automatically serialize model objects
like Django REST Framework does.

So a to_dict() method was added to each model.

Purpose of to_dict():
- convert ORM object into dictionary
- make it JSON-friendly
- send model data in API responses

Example:
{
    "id": 1,
    "name": "Python Programming",
    "code": "CS101",
    "credits": 4
}


=================================================
8. API ROUTES CONNECTED TO ORM
=================================================

The Flask API routes were updated to use database queries.

Implemented routes:
- GET /api/courses/
- POST /api/courses/
- GET /api/courses/<course_id>/
- PUT /api/courses/<course_id>/
- DELETE /api/courses/<course_id>/

These routes now perform ORM CRUD operations and
return JSON responses backed by real database data.


=================================================
9. RELATIONSHIP QUERY ROUTE
=================================================

A route was added to return all students enrolled
in a particular course:

GET /api/courses/<course_id>/students/

This route queries Enrollment records for a course
and returns the related Student records.

This demonstrates how SQLAlchemy relationships can be
used to perform join-style operations in application code.


=================================================
10. LEARNINGS
=================================================

- Configured Flask-SQLAlchemy in a Flask app
- Defined database models using db.Model
- Added relationships between Course Management entities
- Ran migrations using Flask-Migrate
- Inserted data through Flask shell and committed it
- Replaced in-memory data with real database CRUD
- Used to_dict() methods for JSON serialization
- Connected Flask API routes to ORM queries
- Implemented a relationship-based course-students endpoint
"""