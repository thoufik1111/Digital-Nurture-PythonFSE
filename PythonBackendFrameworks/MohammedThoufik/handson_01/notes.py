"""
HANDS-ON 01
Web Framework Foundations & Django Project Setup

1. REQUEST-RESPONSE CYCLE

The Request-Response Cycle is the process through which a web application
receives a request from the user and sends back a response.

Flow:
Browser → URL Routing → View → Model → Database → Response → Browser

Example:
User opens /api/hello/
Django routes the request to hello_view()
The view processes the request and returns a response.


2. MIDDLEWARE

Middleware acts as a bridge between the incoming request and outgoing response.

Common Middleware:
- Authentication Middleware
- Session Middleware
- Security Middleware

Purpose:
- User authentication
- Session handling
- Security checks
- Request/response processing


3. WSGI VS ASGI

WSGI:
- Synchronous
- Handles one request at a time
- Suitable for traditional web applications

ASGI:
- Asynchronous
- Supports WebSockets and real-time applications
- Better for high concurrency

Django supports both WSGI and ASGI.


4. MVC VS MVT

MVC:
Model
View
Controller

Django MVT:
Model
View
Template

Mapping:

MVC Model      → Django Model
MVC View       → Django Template
MVC Controller → Django View

MVT helps Django handle routing and controller logic internally.


5. LEARNINGS

- Understood Django project structure
- Created a Django project and app
- Configured URL routing
- Implemented a basic HTTP response
- Explored Django's MVT architecture
"""