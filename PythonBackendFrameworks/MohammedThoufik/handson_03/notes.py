"""
HANDS-ON 03
Django REST Views, URL Routing & Forms

=================================================
1. DJANGO REST FRAMEWORK (DRF)
=================================================

Django REST Framework is a toolkit used to build
REST APIs in Django applications.

It helps convert Django applications into
backend services that can send and receive JSON data.

Why DRF is useful:
- Easy API development
- Built-in serializers
- Class-based API views
- ViewSets and routers
- Request/Response handling
- Validation support


=================================================
2. SERIALIZERS
=================================================

A serializer converts Django model data into JSON
and also validates incoming JSON data before saving
it into the database.

Example:
Course model object  <-->  JSON response

Serializers created in this hands-on:
- DepartmentSerializer
- CourseSerializer
- StudentSerializer
- EnrollmentSerializer

ModelSerializer is used because it automatically
maps model fields into serializer fields.


=================================================
3. APIVIEW
=================================================

APIView is a DRF class-based view used to build
custom REST endpoints.

In Task 1, APIView was used to create:
- CourseListView
- CourseDetailView

Operations handled:
- GET all courses
- POST new course
- GET one course
- PUT update course
- DELETE course

APIView gives more control but requires writing
methods manually for each operation.


=================================================
4. VIEWSETS
=================================================

A ViewSet is a higher-level DRF abstraction that
combines multiple CRUD operations into one class.

In Task 2, ModelViewSet was used to replace the
manual APIView implementation.

ViewSets created:
- CourseViewSet
- StudentViewSet
- EnrollmentViewSet

Benefits:
- Less code
- Cleaner structure
- Automatic CRUD support
- Easy integration with routers


=================================================
5. ROUTERS
=================================================

Routers automatically generate API URL patterns
for ViewSets.

Example:
router.register('courses', CourseViewSet)

This automatically creates endpoints such as:
- /api/courses/
- /api/courses/1/

This reduces the need to manually define each path
inside urls.py.


=================================================
6. REQUEST AND RESPONSE OBJECTS
=================================================

DRF uses request and response objects for API communication.

request.data
- Used to read incoming JSON payload from POST/PUT requests.

Response(...)
- Used to return JSON data back to the client.

Status codes used:
- 200 OK
- 201 Created
- 204 No Content
- 400 Bad Request
- 404 Not Found


=================================================
7. CUSTOM ACTIONS
=================================================

Custom actions allow additional endpoints to be added
inside a ViewSet using the @action decorator.

In this hands-on, a custom endpoint was created:

/api/courses/{id}/students/

This endpoint returns the students enrolled in
a specific course.


=================================================
8. LEARNINGS
=================================================

- Installed and configured Django REST Framework
- Created serializers for all models
- Built CRUD APIs using APIView
- Performed GET, POST, PUT and DELETE operations
- Configured URL routing for API endpoints
- Refactored API views into ViewSets
- Used DefaultRouter for automatic routing
- Implemented a custom action endpoint
- Understood how DRF handles request and response objects
"""