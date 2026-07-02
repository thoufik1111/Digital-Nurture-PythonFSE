import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import CourseCard from "../components/CourseCard";
import coursesData from "../data/courses";
import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";

function CoursesPage() {
  const [courses] = useState(coursesData);

  const navigate = useNavigate();
  const dispatch = useDispatch();

  function handleEnroll(id) {

  const selectedCourse = courses.find(
    (course) => course.id === id
  );

  if (selectedCourse) {
    dispatch(enroll(selectedCourse));

    alert("Course Enrolled Successfully!");

    navigate("/profile");
  }
}

  return (
    <div style={{ padding: "30px" }}>
      <h1>Courses</h1>

      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          gap: "20px",
        }}
      >
        {courses.map((course) => (
          <div
            key={course.id}
            onClick={() => navigate(`/courses/${course.id}`)}
          >
            <CourseCard
              {...course}
              onEnroll={handleEnroll}
            />
          </div>
        ))}
      </div>
    </div>
  );
}

export default CoursesPage;