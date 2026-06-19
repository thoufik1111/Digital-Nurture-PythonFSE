-- ============================================================
-- HANDS-ON 1
-- Schema Design & Core SQL - DDL and Normalisation
-- Student Course Registration System
-- ============================================================

-- ============================================================
-- TASK 1 : CREATE DATABASE AND TABLES
-- ============================================================

CREATE DATABASE college_db;

USE college_db;

-- ------------------------------------------------------------
-- Departments Table
-- ------------------------------------------------------------

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

-- ------------------------------------------------------------
-- Students Table
-- ------------------------------------------------------------

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

-- ------------------------------------------------------------
-- Courses Table
-- ------------------------------------------------------------

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

-- ------------------------------------------------------------
-- Enrollments Table
-- ------------------------------------------------------------

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2),

    FOREIGN KEY (student_id)
    REFERENCES students(student_id),

    FOREIGN KEY (course_id)
    REFERENCES courses(course_id)
);

-- ------------------------------------------------------------
-- Professors Table
-- ------------------------------------------------------------

CREATE TABLE professors (
    professor_id INT AUTO_INCREMENT PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);



-- ============================================================
-- TASK 2 : NORMALISATION ANALYSIS
-- ============================================================

-- 1NF ANALYSIS
-- All tables contain atomic values.
-- Each column stores only a single value.
-- Example: first_name stores only one name.
-- If multiple phone numbers were stored in one field,
-- it would violate First Normal Form (1NF).

-- 2NF ANALYSIS
-- All non-key attributes depend on the entire primary key.
-- Enrollments represents the relationship between
-- students and courses.
-- Attributes such as enrollment_date and grade
-- depend on the enrollment record itself.
-- Therefore the schema satisfies Second Normal Form (2NF).

-- 3NF ANALYSIS
-- No transitive dependencies exist.
-- Department information is stored separately
-- in the departments table.
-- Students reference departments using department_id.
-- Storing dept_name directly inside students
-- would create redundancy and violate Third Normal Form (3NF).
-- Therefore the schema satisfies Third Normal Form (3NF).



-- ============================================================
-- TASK 3 : ALTER AND EXTEND THE SCHEMA
-- ============================================================

-- Add phone number to students table

ALTER TABLE students
ADD phone_number VARCHAR(15);

-- Add max_seats to courses table

ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

-- Add CHECK constraint for grade validation

ALTER TABLE enrollments
ADD CONSTRAINT chk_grade
CHECK (
    grade IN ('A','B','C','D','F')
    OR grade IS NULL
);

-- Rename hod_name to head_of_dept

ALTER TABLE departments
RENAME COLUMN hod_name TO head_of_dept;

-- Simulate schema rollback by removing phone_number

ALTER TABLE students
DROP COLUMN phone_number;



-- ============================================================
-- VERIFICATION QUERIES
-- ============================================================

DESCRIBE departments;
DESCRIBE students;
DESCRIBE courses;
DESCRIBE enrollments;
DESCRIBE professors;