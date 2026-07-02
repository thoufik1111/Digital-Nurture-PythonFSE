function Header({ siteName, enrolledCount }) {
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
        <a href="#" style={linkStyle}>Home</a>
        <a href="#" style={linkStyle}>Courses</a>
        <a href="#" style={linkStyle}>Profile</a>
      </nav>

      <h3>Enrolled : {enrolledCount}</h3>
    </header>
  );
}

const linkStyle = {
  color: "white",
  marginLeft: "20px",
  textDecoration: "none",
};

export default Header;