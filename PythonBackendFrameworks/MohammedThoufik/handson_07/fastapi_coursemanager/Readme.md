# Hands-On 7 – FastAPI: Dependency Injection, CRUD & OpenAPI Documentation

## Objective

Extend the FastAPI Course Management API by implementing complete CRUD operations, proper HTTP status codes, dependency injection, background tasks, and customized OpenAPI (Swagger) documentation.

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

- FastAPI Dependency Injection (`Depends`)
- CRUD Operations for Courses
- Path Parameters
- Query Parameters
- Response Models
- Proper HTTP Status Codes
- HTTPException Error Handling
- Background Tasks
- OpenAPI / Swagger Customization
- Endpoint Tags
- API Summary & Response Description

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

Application URL:

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
| GET | `/` | API Status |
| GET | `/api/courses/` | List Courses |
| GET | `/api/courses/{id}` | Get Course by ID |
| POST | `/api/courses/` | Create Course |
| PUT | `/api/courses/{id}` | Update Course |
| DELETE | `/api/courses/{id}` | Delete Course |
| GET | `/api/courses/{id}/students` | Get Students Enrolled |
| POST | `/api/enrollments/` | Create Enrollment (Background Task) |

---

## FastAPI Features Demonstrated

- Dependency Injection
- Response Models
- Background Tasks
- HTTPException
- Status Codes (201, 204, 404)
- OpenAPI Metadata
- Swagger UI Tags
- Automatic Request Validation

---

## Expected Outcome

- POST returns **201 Created**.
- DELETE returns **204 No Content**.
- Invalid Course IDs return **404 Not Found**.
- Background task executes after enrollment creation.
- Swagger UI displays grouped endpoints with summaries, descriptions, and response models.
- Dependency Injection and CRUD operations work correctly.

---

## Author

**Mohammed Thoufik**