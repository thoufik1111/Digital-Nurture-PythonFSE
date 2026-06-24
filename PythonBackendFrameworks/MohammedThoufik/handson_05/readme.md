# Hands-On 05

## Topic

Flask with SQLAlchemy ORM & Database Integration

---

## Objective

To integrate SQLAlchemy ORM into the Flask Course Management API, define database models, run database migrations, and replace in-memory route logic with real database CRUD operations.

---

## Tasks Completed

### Task 1 - Define SQLAlchemy Models and Migrations

Configured Flask-SQLAlchemy in the Flask application and initialized the database inside the application factory.

Created the following SQLAlchemy models in `courses/models.py`:

- Department
- Course
- Student
- Enrollment

Implemented model relationships such as:

- Department ↔ Courses
- Department ↔ Students
- Student ↔ Enrollment
- Course ↔ Enrollment

Initialized Flask-Migrate and generated migrations using:

```bash
flask db init
flask db migrate -m "initial schema"
flask db upgrade
```

Verified that the SQLite database and tables were created successfully.

Inserted sample data into the database using the Flask shell and committed records with `db.session.commit()`.

---

### Task 2 - Connect ORM to API Routes

Replaced the in-memory course list used in Hands-On 04 with actual database queries.

Updated the course API routes to use SQLAlchemy ORM for CRUD operations:

- `GET /api/courses/`
- `POST /api/courses/`
- `GET /api/courses/<course_id>/`
- `PUT /api/courses/<course_id>/`
- `DELETE /api/courses/<course_id>/`

Added `to_dict()` methods in all models to serialize ORM objects into JSON-friendly dictionaries.

Implemented a course-students route:

- `GET /api/courses/<course_id>/students/`

This route fetches students enrolled in a specific course using the Enrollment relationship.

---

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite

---

## Outcome

Successfully integrated a real database into the Flask Course Management API, created ORM models and relationships, applied database migrations, performed CRUD operations using SQLAlchemy, and exposed course data through JSON API endpoints backed by the database.