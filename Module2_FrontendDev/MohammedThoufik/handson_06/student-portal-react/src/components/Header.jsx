import { Link } from "react-router-dom";
import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";
import { useSelector }
from "react-redux";
function Header({ siteName }) {
 const enrolledCourses =
useSelector(
state => state.enrollment.enrolledCourses
);
  return (
    <header
      style={{
        background: "#1e3a8a",
        color: "white",
        padding: "15px 30px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <div>
        <h2>{siteName}</h2>
      </div>

      <nav>

        <Link to="/" style={linkStyle}>
          Home
        </Link>
      
        <Link to="/courses" style={linkStyle}>
          Courses
        </Link>
      
        <Link to="/profile" style={linkStyle}>
          Profile
        </Link>
      
         </nav>

      <h3>Enrolled : {enrolledCourses.length}</h3>
    </header>
  );
}

const linkStyle = {
  color: "white",
  marginLeft: "20px",
  textDecoration: "none",
};

export default Header;