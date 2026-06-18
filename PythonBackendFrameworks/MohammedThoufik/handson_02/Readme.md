# Hands-On 02

## Topic

Django Models, ORM & Admin Interface

---

## Objective

To design database models for a Course Management System, perform database migrations, execute ORM queries, and manage records using Django Admin.

---

## Tasks Completed

### Task 1 - Models and Migrations

Created the following models:

- Department
- Course
- Student
- Enrollment

Implemented:

- Primary Keys
- Foreign Keys
- Unique Constraints
- Model Relationships
- __str__ Methods

Generated and applied migrations using:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Task 2 - Django ORM Queries

Performed:

- Object Creation
- Data Retrieval
- Filtering
- Aggregation using Count()
- Updates using F() Expressions
- Relationship Traversal using Foreign Keys

### Task 3 - Django Admin Interface

Configured Django Admin.

Registered:

- Department
- Course
- Student
- Enrollment

Customized Course Admin with:

- list_display
- search_fields
- list_filter

Created records through the admin interface and verified unique enrollment constraints.

---

## Technologies Used

- Python
- Django
- SQLite

---

## Outcome

Successfully implemented database models, established relationships between entities, executed ORM operations, applied migrations, and managed data through Django Admin Interface.