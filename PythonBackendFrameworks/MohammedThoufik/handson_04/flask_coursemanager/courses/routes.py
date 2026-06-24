from flask import Blueprint, jsonify, request

courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")

# Temporary in-memory data store for Handson 04
courses_data = [
    {"id": 1, "name": "Python Programming", "code": "CS101", "credits": 4},
    {"id": 2, "name": "Database Management Systems", "code": "CS102", "credits": 3}
]


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
    return make_response_json(courses_data, 200)


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

    new_course = {
        "id": len(courses_data) + 1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses_data.append(new_course)
    return make_response_json(new_course, 201)


@courses_bp.route("/<int:course_id>/", methods=["GET"])
def get_course(course_id):
    course = next((c for c in courses_data if c["id"] == course_id), None)

    if not course:
        return make_error_json("Course not found", 404)

    return make_response_json(course, 200)


@courses_bp.route("/<int:course_id>/", methods=["PUT"])
def update_course(course_id):
    course = next((c for c in courses_data if c["id"] == course_id), None)

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

    course["name"] = data["name"]
    course["code"] = data["code"]
    course["credits"] = data["credits"]

    return make_response_json(course, 200)


@courses_bp.route("/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):
    course = next((c for c in courses_data if c["id"] == course_id), None)

    if not course:
        return make_error_json("Course not found", 404)

    courses_data.remove(course)

    return jsonify({
        "status": "success",
        "message": f"Course with id {course_id} deleted successfully"
    }), 200