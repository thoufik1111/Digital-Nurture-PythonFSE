"""
HANDS-ON 02
Django Models, ORM & Admin Interface

=================================================
1. DJANGO MODELS
=================================================

Django Models are Python classes that define the
structure of database tables.

Each model maps to a database table and each
attribute maps to a table column.

Example:

class Course(models.Model):
    name = models.CharField(max_length=100)

This creates a table named Course with a column
called name.

Benefits:
- Reduces manual SQL writing
- Provides database abstraction
- Supports multiple database systems


=================================================
2. FIELD TYPES & CONSTRAINTS
=================================================

Common Field Types:

CharField
- Stores short text values.

EmailField
- Stores email addresses.
- Can enforce uniqueness.

IntegerField
- Stores integer values.

DecimalField
- Stores decimal numbers.

DateField
- Stores date values.

ForeignKey
- Creates relationships between tables.


Constraints Used:

PRIMARY KEY
- Uniquely identifies each record.

UNIQUE
- Prevents duplicate values.

NULL
- Allows empty values.

FOREIGN KEY
- Maintains referential integrity.


=================================================
3. DJANGO ORM
=================================================

ORM stands for Object Relational Mapping.

ORM allows interaction with databases using
Python code instead of raw SQL queries.

Examples:

Create:

Department.objects.create(
    name="Computer Science"
)

Read:

Department.objects.all()

Filter:

Course.objects.filter(
    department__name="Computer Science"
)

Update:

Department.objects.update(
    budget=500000
)

Delete:

Department.objects.filter(
    id=1
).delete()


Advantages:
- Cleaner code
- Database independent
- Faster development
- Better maintainability


=================================================
4. MIGRATIONS
=================================================

Migrations are Django's way of applying model
changes to the database.

Commands:

python manage.py makemigrations

Generates migration files.

python manage.py migrate

Applies changes to the database.

python manage.py showmigrations

Displays migration status.


=================================================
5. DJANGO ADMIN INTERFACE
=================================================

Django provides a built-in administration panel.

Features:

- Create records
- View records
- Update records
- Delete records
- Search data
- Filter data

Admin URL:

http://127.0.0.1:8000/admin/

Models must be registered inside admin.py
before they appear in the admin panel.


=================================================
6. MODEL RELATIONSHIPS
=================================================

Department
     |
     |
     v
Course

Department
     |
     |
     v
Student

Student
     |
     |
Enrollment
     |
     |
     v
Course

These relationships are implemented using
ForeignKey fields.


=================================================
7. LEARNINGS
=================================================

- Created Django Models
- Applied Database Migrations
- Implemented Foreign Key Relationships
- Executed ORM Queries
- Used annotate() and Count()
- Used F() Expressions
- Configured Django Admin Panel
- Implemented Unique Constraints
"""