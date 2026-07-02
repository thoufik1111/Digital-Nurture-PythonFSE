function CourseCard({
  id,
  name,
  code,
  credits,
  grade,
  onEnroll,
}) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: "10px",
        padding: "20px",
        width: "260px",
        background: "white",
        boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
      }}
    >
      <h3>{name}</h3>

      <p><strong>Code:</strong> {code}</p>

      <p><strong>Credits:</strong> {credits}</p>

      <p><strong>Grade:</strong> {grade}</p>

      <button
  onClick={(e) => {
    e.stopPropagation();
    console.log("Button clicked");
    console.log("onEnroll prop:", onEnroll);
    onEnroll(id);
  }}
>
  Enroll
</button>
    </div>
  );
}

export default CourseCard;