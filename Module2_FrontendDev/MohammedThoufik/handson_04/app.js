import { courses } from "./data.js";

/* ==================================================
   GLOBAL DOM REFERENCES
================================================== */
const courseGrid = document.querySelector(".course-grid");
const totalCreditsElement = document.querySelector("#total-credits");
const selectedCourseElement = document.querySelector("#selected-course");
const searchInput = document.querySelector("#search-courses");
const sortButton = document.querySelector("#sort-credits-btn");
const courseLoadingElement = document.querySelector("#course-loading");

const notificationsGrid = document.querySelector(".notifications-grid");
const notificationsLoading = document.querySelector("#notifications-loading");
const notificationsError = document.querySelector("#notifications-error");
const retryButton = document.querySelector("#retry-btn");
const loadNotificationsBtn = document.querySelector("#load-notifications-btn");
const simulateErrorBtn = document.querySelector("#simulate-error-btn");
const loadUser1PostsBtn = document.querySelector("#load-user1-posts-btn");

let displayedCourses = [];
let lastNotificationFetchType = "normal";

/* ==================================================
   TASK 1 - PROMISES & ASYNC/AWAIT
================================================== */

// 45. fetchUser using Promise chaining
function fetchUser(id) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then((response) => response.json())
    .then((user) => {
      console.log(`Promise chain user ${id}:`, user.name);
      return user;
    });
}

// 46. fetchUser rewritten using async/await + try/catch
async function fetchUserAsync(id) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    const user = await response.json();
    console.log(`Async/await user ${id}:`, user.name);
    return user;
  } catch (error) {
    console.error(`Error fetching user ${id}:`, error);
  }
}

// 47. Simulate delayed course fetch
function fetchAllCourses() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(courses);
    }, 1000);
  });
}

// 49. Promise.all demo
Promise.all([fetchUser(1), fetchUser(2)])
  .then(([user1, user2]) => {
    console.log("Promise.all users:", user1.name, "and", user2.name);
  })
  .catch((error) => {
    console.error("Promise.all error:", error);
  });

// Also call async version once for demonstration
fetchUserAsync(3);

/* ==================================================
   COURSE RENDERING
================================================== */
function renderCourses(courseArray) {
  courseGrid.innerHTML = "";

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

  const totalCredits = courseArray.reduce(
    (sum, course) => sum + course.credits,
    0
  );

  totalCreditsElement.textContent = `Total Credits Enrolled: ${totalCredits}`;
}

/* ==================================================
   TASK 1 - LOAD COURSES AFTER 1 SECOND DELAY
================================================== */
async function loadCourses() {
  courseLoadingElement.classList.remove("hidden");
  courseGrid.innerHTML = "";
  totalCreditsElement.textContent = "";

  displayedCourses = await fetchAllCourses();

  courseLoadingElement.classList.add("hidden");
  renderCourses(displayedCourses);
}

/* ==================================================
   TASK 2 - FETCH API WITH ERROR HANDLING
================================================== */

// Fetch version kept for Task 2 learning
async function apiFetchUsingFetch(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return await response.json();
}

/* ==================================================
   TASK 3 - AXIOS VERSION OF apiFetch
================================================== */

// Request interceptor
axios.interceptors.request.use((config) => {
  console.log(`API call started: ${config.url}`);
  return config;
});

/*
Fetch vs Axios - 3 differences
1. Fetch is built into the browser; Axios is an external library.
2. Fetch requires manual response.json() parsing; Axios auto-parses JSON.
3. Fetch does not reject on HTTP 404/500 by default; Axios throws automatically for non-2xx responses.
*/
async function apiFetch(url, params = {}) {
  const response = await axios.get(url, {
    params,
    timeout: 5000
  });

  return response.data;
}

/* ==================================================
   NOTIFICATION RENDERING
================================================== */
function renderNotifications(posts) {
  notificationsGrid.innerHTML = "";

  posts.slice(0, 8).forEach((post) => {
    const card = document.createElement("article");
    card.className = "notification-card";

    card.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.body}</p>
    `;

    notificationsGrid.appendChild(card);
  });
}

function showNotificationLoading() {
  notificationsLoading.classList.remove("hidden");
  notificationsError.classList.add("hidden");
  retryButton.classList.add("hidden");
  notificationsGrid.innerHTML = "";
}

function hideNotificationLoading() {
  notificationsLoading.classList.add("hidden");
}

function showNotificationError(message) {
  notificationsError.textContent = message;
  notificationsError.classList.remove("hidden");
  retryButton.classList.remove("hidden");
}

/* ==================================================
   LOAD NOTIFICATIONS - NORMAL
================================================== */
async function loadNotifications() {
  lastNotificationFetchType = "normal";
  showNotificationLoading();

  try {
    const posts = await apiFetch("https://jsonplaceholder.typicode.com/posts");
    hideNotificationLoading();
    renderNotifications(posts);
  } catch (error) {
    hideNotificationLoading();
    showNotificationError(
      "Unable to load notifications right now. Please try again."
    );
    console.log("Simulated 404 handled successfully");
  }
}

/* ==================================================
   SIMULATE ERROR WITH BAD URL
================================================== */
async function loadNotificationsWithError() {
  lastNotificationFetchType = "error";
  showNotificationLoading();

  try {
    await apiFetch("https://jsonplaceholder.typicode.com/nonexistent");
    hideNotificationLoading();
  } catch (error) {
    hideNotificationLoading();
    showNotificationError(
      "Oops! Notifications could not be loaded because the resource was not found."
    );
    console.log("Simulated 404 handled successfully");
  }
}

/* ==================================================
   AXIOS PARAMS EXAMPLE - USER 1 POSTS
================================================== */
async function loadUser1Posts() {
  lastNotificationFetchType = "user1";
  showNotificationLoading();

  try {
    const posts = await apiFetch(
      "https://jsonplaceholder.typicode.com/posts",
      { userId: 1 }
    );

    hideNotificationLoading();
    renderNotifications(posts);
  } catch (error) {
    hideNotificationLoading();
    showNotificationError(
      "Could not load User 1 posts. Please try again."
    );
    console.log("Simulated 404 handled successfully");
  }
}

/* ==================================================
   EVENT LISTENERS - COURSES
================================================== */
searchInput.addEventListener("input", (event) => {
  const searchValue = event.target.value.toLowerCase();

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchValue)
  );

  displayedCourses = filteredCourses;
  renderCourses(displayedCourses);
});

sortButton.addEventListener("click", () => {
  displayedCourses = [...displayedCourses].sort((a, b) => b.credits - a.credits);
  renderCourses(displayedCourses);
});

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

/* ==================================================
   EVENT LISTENERS - NOTIFICATIONS
================================================== */
loadNotificationsBtn.addEventListener("click", loadNotifications);
simulateErrorBtn.addEventListener("click", loadNotificationsWithError);
loadUser1PostsBtn.addEventListener("click", loadUser1Posts);

retryButton.addEventListener("click", () => {
  if (lastNotificationFetchType === "error") {
    loadNotifications();
  } else if (lastNotificationFetchType === "user1") {
    loadUser1Posts();
  } else {
    loadNotifications();
  }
});

/* ==================================================
   INITIAL PAGE LOAD
================================================== */
loadCourses();