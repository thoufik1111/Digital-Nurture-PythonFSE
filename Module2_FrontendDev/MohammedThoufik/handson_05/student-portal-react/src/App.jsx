import { useState, useEffect } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {
  const [courses, setCourses] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [searchTerm, setSearchTerm] = useState("");

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Runs once after component mounts
  useEffect(() => {
    async function fetchCourses() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

        const data = await response.json();

        const courseData = data.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS10${index + 1}`,
          credits: 3 + (index % 2),
          grade: "A",
        }));

        setCourses(courseData);
      } catch (err) {
        setError("Unable to load courses.");
      } finally {
        setLoading(false);
      }
    }

    fetchCourses();
  }, []);

  // Runs whenever courses change
  useEffect(() => {
    console.log("Courses updated");
    // Dependency array [courses] means this effect runs only when
    // the courses state changes, avoiding unnecessary executions.
  }, [courses]);

  function handleEnroll(courseId) {
    if (!enrolledCourses.includes(courseId)) {
      setEnrolledCourses([...enrolledCourses, courseId]);
    }
  }

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <main style={{ padding: "40px" }}>
        <h2>Available Courses</h2>

        <input
          type="text"
          placeholder="Search Course..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{
            padding: "10px",
            width: "300px",
            marginBottom: "25px",
          }}
        />

        {loading && <h3>Loading...</h3>}

        {error && <h3 style={{ color: "red" }}>{error}</h3>}

        {!loading && !error && (
          <div
            style={{
              display: "flex",
              gap: "20px",
              flexWrap: "wrap",
            }}
          >
            {filteredCourses.map((course) => (
              <CourseCard
                key={course.id}
                {...course}
                onEnroll={handleEnroll}
              />
            ))}
          </div>
        )}

        <StudentProfile />
      </main>

      <Footer />
    </>
  );
}

export default App;