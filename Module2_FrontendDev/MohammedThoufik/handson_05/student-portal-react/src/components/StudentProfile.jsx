import { useState } from "react";

function StudentProfile() {
  const [profile, setProfile] = useState({
    name: "",
    email: "",
    semester: "",
  });

  function handleChange(event) {
    const { name, value } = event.target;

    setProfile((prevProfile) => ({
      ...prevProfile,
      [name]: value,
    }));
  }

  return (
    <div
      style={{
        marginTop: "40px",
        padding: "20px",
        border: "1px solid #ddd",
        borderRadius: "10px",
        background: "#fff",
      }}
    >
      <h2>Student Profile</h2>

      <input
        type="text"
        name="name"
        placeholder="Name"
        value={profile.name}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="email"
        name="email"
        placeholder="Email"
        value={profile.email}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="text"
        name="semester"
        placeholder="Semester"
        value={profile.semester}
        onChange={handleChange}
      />

      <hr />

      <h3>Preview</h3>

      <p>Name : {profile.name}</p>

      <p>Email : {profile.email}</p>

      <p>Semester : {profile.semester}</p>
    </div>
  );
}

export default StudentProfile;