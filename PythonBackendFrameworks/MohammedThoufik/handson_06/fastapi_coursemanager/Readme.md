# Hands-On 6 – FastAPI: Path Parameters, Pydantic & Async Endpoints

## Objective

Build a Course Management REST API using FastAPI with Pydantic validation, asynchronous endpoints, path/query parameters, and automatic Swagger documentation.

---

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

---

## Project Structure

```
fastapi_coursemanager/
│
├── main.py
├── schemas.py
├── database.py
├── requirements.txt
└── README.md
```

---

## Features Implemented

- FastAPI application setup
- Root endpoint (`GET /`)
- Create Course API (`POST /api/courses/`)
- Pydantic request validation
- Nested response schemas
- Path Parameters
- Query Parameters
- Pagination
- Department filtering
- Dependency Injection using `Depends()`
- Automatic Swagger/OpenAPI Documentation
- Async API endpoints

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check API status |
| POST | `/api/courses/` | Create a new course |
| GET | `/api/courses/` | Get all courses with pagination/filtering |
| GET | `/api/courses/{course_id}` | Get a course by ID |

---

## Sample Request

```json
{
  "name": "Data Structures",
  "code": "CS101",
  "credits": 4,
  "department_id": 1
}
```

---

## Expected Outcome

- FastAPI application runs successfully.
- Swagger UI is generated automatically.
- Course creation uses Pydantic validation.
- Invalid requests return HTTP 422 validation errors.
- Path parameters work correctly.
- Query parameters support pagination and filtering.
- Async endpoints execute successfully.

---

## Author

**Mohammed Thoufik**