# Hands-On 03

## Topic

Django REST Views, URL Routing & Forms

---

## Objective

To build REST API endpoints for the Course Management System using Django REST Framework, implement CRUD operations, and expose model data through serializers, views, viewsets, and routers.

---

## Tasks Completed

### Task 1 - Serializers and Basic API Views

Created serializers for all models:

- DepartmentSerializer
- CourseSerializer
- StudentSerializer
- EnrollmentSerializer

Implemented API endpoints for Course using DRF APIView:

- GET `/api/courses/`
- POST `/api/courses/`
- GET `/api/courses/<id>/`
- PUT `/api/courses/<id>/`
- DELETE `/api/courses/<id>/`

This task was used to understand how CRUD APIs can be built manually using APIView and serializers.

---

### Task 2 - ViewSets and Routers

Refactored the API implementation using DRF ModelViewSet and DefaultRouter.

Implemented:

- CourseViewSet
- StudentViewSet
- EnrollmentViewSet

Configured automatic routing for:

- `/api/courses/`
- `/api/students/`
- `/api/enrollments/`

Added a custom action endpoint:

- `/api/courses/<id>/students/`

This endpoint returns all students enrolled in a specific course.

---

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite

---

## Outcome

Successfully built REST APIs for the Course Management System, implemented CRUD operations using DRF, tested endpoints using API requests, and refactored manual views into ViewSets with router-based URL routing.