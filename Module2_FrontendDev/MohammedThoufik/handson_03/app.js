import { courses } from "./data.js";

/* --------------------------------------------------
   TASK 1 - ES6+ SYNTAX PRACTICE
-------------------------------------------------- */

// Destructuring in a loop
courses.forEach((course) => {
  const { name, credits } = course;
  console.log(`Course: ${name}, Credits: ${credits}`);
});

// Array.map() -> formatted strings
const formattedCourses = courses.map(
  (course) => `${course.code} — ${course.name} (${course.credits} credits)`
);
console.log("Formatted Courses:", formattedCourses);

// Array.filter() -> courses with credits >= 4
const highCreditCourses = courses.filter((course) => course.credits >= 4);
console.log("Courses with credits >= 4:", highCreditCourses);
console.log("High credit course count:", highCreditCourses.length);

// Array.reduce() -> total credits
const totalCredits = courses.reduce(
  (total, course) => total + course.credits,
  0
);
console.log("Total Credits:", totalCredits);

/* --------------------------------------------------
   TASK 2 - DOM SELECTION & DYNAMIC RENDERING
-------------------------------------------------- */

const courseGrid = document.querySelector(".course-grid");
const totalCreditsElement = document.querySelector("#total-credits");
const selectedCourseElement = document.querySelector("#selected-course");
const searchInput = document.querySelector("#search-courses");
const sortButton = document.querySelector("#sort-credits-btn");

// We will use this for rendering and filtering
let displayedCourses = [...courses];

/**
 * Render courses into the course grid
 */
function renderCourses(courseArray) {
  // Clear old cards before re-rendering
  courseGrid.innerHTML = "";

  // Create course cards dynamically
  courseArray.forEach((course) => {
    const article = document.createElement("article");
    article.className = "course-card";
    article.dataset.id = course.id;

    article.innerHTML = `
      <h3>${course.name}</h3>
      <p><strong>Course Code:</strong> ${course.code}</p>
      <p><strong>Credits:</strong> ${course.credits}</p>
      <span>Grade: ${course.grade}</span>
    `;

    courseGrid.appendChild(article);
  });

  // Update total credits dynamically
  const currentTotalCredits = courseArray.reduce(
    (sum, course) => sum + course.credits,
    0
  );

  totalCreditsElement.textContent = `Total Credits Enrolled: ${currentTotalCredits}`;
}

/* --------------------------------------------------
   TASK 3 - EVENT LISTENERS & INTERACTIVITY
-------------------------------------------------- */

// Search courses by name
searchInput.addEventListener("input", (event) => {
  const searchValue = event.target.value.toLowerCase();

  displayedCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchValue)
  );

  renderCourses(displayedCourses);
});

// Sort by credits descending
sortButton.addEventListener("click", () => {
  displayedCourses = [...displayedCourses].sort(
    (a, b) => b.credits - a.credits
  );

  renderCourses(displayedCourses);
});

// Event delegation for course card click
courseGrid.addEventListener("click", (event) => {
  const clickedCard = event.target.closest(".course-card");

  if (!clickedCard) return;

  const courseId = Number(clickedCard.dataset.id);
  const selectedCourse = courses.find((course) => course.id === courseId);

  if (selectedCourse) {
    selectedCourseElement.innerHTML = `
      <div class="selected-course-box">
        <h3>Selected Course</h3>
        <p><strong>Name:</strong> ${selectedCourse.name}</p>
        <p><strong>Code:</strong> ${selectedCourse.code}</p>
        <p><strong>Credits:</strong> ${selectedCourse.credits}</p>
        <p><strong>Grade:</strong> ${selectedCourse.grade}</p>
      </div>
    `;
  }
});

// Initial render
renderCourses(displayedCourses);