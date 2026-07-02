import StudentProfile from "../components/StudentProfile";

import { useSelector, useDispatch } from "react-redux";

import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  const dispatch = useDispatch();

  return (

    <div style={{ padding: "30px" }}>

      <h1>Student Profile</h1>

      <StudentProfile />

      <hr />

      <h2>Enrolled Courses</h2>

      {
        enrolledCourses.length === 0 ?

          <p>No enrolled courses.</p>

          :

          enrolledCourses.map((course) => (

            <div
              key={course.id}
              style={{
                marginBottom: "15px",
                borderBottom: "1px solid gray"
              }}
            >

              <h3>{course.name}</h3>

              <button
                onClick={() => dispatch(unenroll(course.id))}
              >
                Remove
              </button>

            </div>

          ))
      }

    </div>

  );

}

export default ProfilePage;