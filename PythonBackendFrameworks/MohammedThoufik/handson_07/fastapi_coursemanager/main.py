from fastapi import FastAPI
from schemas import CourseCreate
from fastapi import Depends
from schemas import CourseUpdate
from database import get_db
from fastapi import status, HTTPException
from schemas import CourseResponse
from fastapi import BackgroundTasks
def send_confirmation_email(email: str):

    print(
        f"Sending confirmation to {email}"
    )
app = FastAPI(

    title="Course Management API",

    description="FastAPI backend for Course Management System",

    version="1.0",

    contact={
        "name":"Mohammed Thoufik",
        "email":"thoufik@example.com"
    }

)

courses = []


@app.get("/",tags=["Courses"])
async def root():
    return {
        "message": "API running"
    }


@app.post(

    "/api/courses/",

    tags=["Courses"],

    summary="Create a new course",

    response_description="Course created successfully",

    response_model=CourseResponse,

    status_code=status.HTTP_201_CREATED

)
async def create_course(course: CourseCreate):

    new_course = course.model_dump()

    new_course["id"] = len(courses) + 1

    courses.append(new_course)

    return new_course
@app.get(
    "/api/courses/{course_id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def get_course(course_id: int):

    for course in courses:

        if course["id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )
@app.get("/api/courses/",tags=["Courses"])
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None,
    db=Depends(get_db)
):

    result = courses

    if department_id is not None:
        result = [
            c for c in result
            if c["department_id"] == department_id
        ]

    return result[skip: skip + limit]
@app.put("/api/courses/{course_id}",tags=["Courses"])
async def update_course(
    course_id: int,
    course: CourseUpdate
):

    for c in courses:

        if c["id"] == course_id:

            updated = course.model_dump(exclude_unset=True)

            c.update(updated)

            return c

    raise HTTPException(
    status_code=404,
    detail="Course not found"
)
@app.delete(
    "/api/courses/{course_id}",
    tags=["Courses"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(course_id: int):

    for course in courses:

        if course["id"] == course_id:

            courses.remove(course)

            return

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )
students = [
    {
        "id": 1,
        "name": "Mohammed Thoufik",
        "course_id": 1
    },
    {
        "id": 2,
        "name": "Dhanush",
        "course_id": 1
    }
]
@app.get("/api/courses/{course_id}/students",tags=["Students"])
async def get_students(course_id: int):

    return [
        s
        for s in students
        if s["course_id"] == course_id
    ]
@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    status_code=status.HTTP_201_CREATED
)
async def create_enrollment(
    background_tasks: BackgroundTasks
):

    background_tasks.add_task(
        send_confirmation_email,
        "student@example.com"
    )

    return {
        "message": "Enrollment created"
    }