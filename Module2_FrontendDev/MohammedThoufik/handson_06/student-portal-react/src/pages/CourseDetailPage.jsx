import { useParams } from "react-router-dom";
import courses from "../data/courses";

function CourseDetailPage() {

  const { courseId } = useParams();

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return <h2>Course not found</h2>;
  }

  return (
    <div style={{ padding: "30px" }}>

      <h1>{course.name}</h1>

      <p><strong>Code :</strong> {course.code}</p>

      <p><strong>Credits :</strong> {course.credits}</p>

      <p><strong>Grade :</strong> {course.grade}</p>

    </div>
  );
}

export default CourseDetailPage;