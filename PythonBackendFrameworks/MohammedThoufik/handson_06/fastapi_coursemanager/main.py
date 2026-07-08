from fastapi import FastAPI
from schemas import CourseCreate
from fastapi import Depends
from schemas import CourseUpdate
from database import get_db
app = FastAPI(
    title="Course Management API",
    version="1.0"
)

courses = []


@app.get("/")
async def root():
    return {
        "message": "API running"
    }


@app.post("/api/courses/")
async def create_course(course: CourseCreate):

    new_course = course.model_dump()

    new_course["id"] = len(courses) + 1

    courses.append(new_course)

    return new_course
@app.get("/api/courses/{course_id}")
async def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course

    return {"message": "Course not found"}
@app.get("/api/courses/")
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
@app.put("/api/courses/{course_id}")
async def update_course(
    course_id: int,
    course: CourseUpdate
):

    for c in courses:

        if c["id"] == course_id:

            updated = course.model_dump(exclude_unset=True)

            c.update(updated)

            return c

    return {"message":"Course not found"}