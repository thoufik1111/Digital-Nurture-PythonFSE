from flask import Blueprint, jsonify, request
from .models import db, Course, Student, Enrollment

courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")


def make_response_json(data, status_code=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


def make_error_json(message, status_code=400):
    return jsonify({
        "status": "error",
        "message": message
    }), status_code


@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return make_response_json([course.to_dict() for course in courses], 200)


@courses_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    if data is None:
        return make_error_json("Request body must be valid JSON", 400)

    required_fields = ["name", "code", "credits"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return make_error_json(
            f"Missing required fields: {', '.join(missing_fields)}", 400
        )

    new_course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data.get("department_id")
    )

    db.session.add(new_course)
    db.session.commit()

    return make_response_json(new_course.to_dict(), 201)


@courses_bp.route("/<int:course_id>/", methods=["GET"])
def get_course(course_id):
    course = Course.query.get(course_id)

    if not course:
        return make_error_json("Course not found", 404)

    return make_response_json(course.to_dict(), 200)


@courses_bp.route("/<int:course_id>/", methods=["PUT"])
def update_course(course_id):
    course = Course.query.get(course_id)

    if not course:
        return make_error_json("Course not found", 404)

    data = request.get_json()

    if data is None:
        return make_error_json("Request body must be valid JSON", 400)

    required_fields = ["name", "code", "credits"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return make_error_json(
            f"Missing required fields: {', '.join(missing_fields)}", 400
        )

    course.name = data["name"]
    course.code = data["code"]
    course.credits = data["credits"]
    course.department_id = data.get("department_id")

    db.session.commit()

    return make_response_json(course.to_dict(), 200)


@courses_bp.route("/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get(course_id)

    if not course:
        return make_error_json("Course not found", 404)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": f"Course with id {course_id} deleted successfully"
    }), 200


@courses_bp.route("/<int:course_id>/students/", methods=["GET"])
def get_students_for_course(course_id):
    course = Course.query.get(course_id)

    if not course:
        return make_error_json("Course not found", 404)

    enrollments = Enrollment.query.filter_by(course_id=course_id).all()
    students = [enrollment.student.to_dict() for enrollment in enrollments]

    return make_response_json(students, 200)