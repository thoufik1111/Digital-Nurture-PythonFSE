
USE college_db;

INSERT IGNORE INTO enrollments(student_id,course_id,enrollment_date,grade)
VALUES
(1,3,'2022-07-02','A'),
(2,2,'2022-07-02','A'),
(5,3,'2022-07-02','B'),
(9,1,'2022-07-02','A'),
(9,2,'2022-07-02','A'),
(9,3,'2022-07-02','A'),
(10,4,'2022-07-02','B');

-- Q1 Students enrolled in more courses than average

SELECT
s.student_id,
CONCAT(s.first_name,' ',s.last_name) AS student_name,
COUNT(e.course_id) total_courses
FROM students s
JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY s.student_id,s.first_name,s.last_name
HAVING COUNT(e.course_id)>
(
SELECT AVG(course_count)
FROM
(
SELECT COUNT(*) course_count
FROM enrollments
GROUP BY student_id
) avg_enrollments
);

-- Q2 Courses where every enrolled student scored A

SELECT c.course_name,c.course_code
FROM courses c
WHERE NOT EXISTS
(
SELECT *
FROM enrollments e
WHERE e.course_id=c.course_id
AND e.grade<>'A'
);

-- Q3 Highest paid professor in every department

SELECT
p.prof_name,
d.dept_name,
p.salary
FROM professors p
JOIN departments d
ON p.department_id=d.department_id
WHERE p.salary=
(
SELECT MAX(p2.salary)
FROM professors p2
WHERE p2.department_id=p.department_id
);

-- Q4 Departments whose average professor salary > 85000

SELECT *
FROM
(
SELECT
d.dept_name,
AVG(p.salary) average_salary
FROM departments d
JOIN professors p
ON d.department_id=p.department_id
GROUP BY d.department_id,d.dept_name
) dept_avg
WHERE average_salary>85000;

CREATE OR REPLACE VIEW vw_student_enrollment_summary AS
SELECT
s.student_id,
CONCAT(s.first_name,' ',s.last_name) student_name,
d.dept_name,
COUNT(e.course_id) total_courses,
ROUND(AVG(
CASE
WHEN e.grade='A' THEN 4
WHEN e.grade='B' THEN 3
WHEN e.grade='C' THEN 2
WHEN e.grade='D' THEN 1
ELSE 0
END),2) GPA
FROM students s
JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY s.student_id,student_name,d.dept_name;

SELECT * FROM vw_student_enrollment_summary;

CREATE OR REPLACE VIEW vw_course_stats AS
SELECT
c.course_name,
c.course_code,
COUNT(e.student_id) total_enrollments,
ROUND(AVG(
CASE
WHEN e.grade='A' THEN 4
WHEN e.grade='B' THEN 3
WHEN e.grade='C' THEN 2
WHEN e.grade='D' THEN 1
ELSE 0
END),2) avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_id,c.course_name,c.course_code;

SELECT * FROM vw_course_stats;

SELECT *
FROM vw_student_enrollment_summary
WHERE GPA>3;

-- Multi-table views are generally not updatable.
UPDATE vw_student_enrollment_summary
SET dept_name='Test'
WHERE student_id=1;

DROP VIEW vw_course_stats;
DROP VIEW vw_student_enrollment_summary;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
student_id,
first_name,
last_name,
department_id
FROM students
WHERE department_id=1
WITH CHECK OPTION;

SELECT * FROM vw_student_enrollment_summary;

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
IN p_student INT,
IN p_course INT,
IN p_date DATE
)
BEGIN

IF EXISTS(
SELECT 1
FROM enrollments
WHERE student_id=p_student
AND course_id=p_course
)
THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT='Student already enrolled in this course';
ELSE
INSERT INTO enrollments(student_id,course_id,enrollment_date,grade)
VALUES(p_student,p_course,p_date,NULL);
END IF;

END$$

DELIMITER ;

CALL sp_enroll_student(10,2,'2026-07-01');
SELECT * FROM enrollments WHERE student_id=10;

CREATE TABLE IF NOT EXISTS department_transfer_log(
log_id INT AUTO_INCREMENT PRIMARY KEY,
student_id INT,
old_department INT,
new_department INT,
transfer_date DATETIME
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
IN p_student INT,
IN p_new_department INT
)
BEGIN

DECLARE old_dept INT;

START TRANSACTION;

SELECT department_id
INTO old_dept
FROM students
WHERE student_id=p_student;

UPDATE students
SET department_id=p_new_department
WHERE student_id=p_student;

INSERT INTO department_transfer_log
(student_id,old_department,new_department,transfer_date)
VALUES
(p_student,old_dept,p_new_department,NOW());

COMMIT;

END$$

DELIMITER ;

CALL sp_transfer_student(10,3);

SELECT * FROM department_transfer_log;

-- Rollback demo

START TRANSACTION;

UPDATE students
SET department_id=2
WHERE student_id=9;

ROLLBACK;

SELECT student_id,department_id
FROM students
WHERE student_id=9;

-- SAVEPOINT demo

START TRANSACTION;

INSERT INTO enrollments(student_id,course_id,enrollment_date,grade)
VALUES(10,5,'2026-08-01','A');

SAVEPOINT first_insert;

-- This duplicate should fail if already exists
INSERT INTO enrollments(student_id,course_id,enrollment_date,grade)
VALUES(10,5,'2026-08-02','A');

ROLLBACK TO first_insert;

COMMIT;

SELECT * FROM enrollments WHERE student_id=10;
-- ============================================================
-- HANDS-ON 4
-- Query Optimisation - Indexes, EXPLAIN & Performance
-- ============================================================

USE college_db;

-- ============================================================
-- TASK 1 : BASELINE PERFORMANCE (WITHOUT INDEXES)
-- ============================================================

/*
Running EXPLAIN helps understand how MySQL executes
the query before actually running it.

Initially, MySQL may perform a Full Table Scan
because indexes are not yet available.
*/

EXPLAIN FORMAT=JSON

SELECT
s.first_name,
s.last_name,
c.course_name

FROM enrollments e

JOIN students s
ON s.student_id=e.student_id

JOIN courses c
ON c.course_id=e.course_id

WHERE s.enrollment_year=2022;



/*
--------------------------------------------------------------
Expected Observation

• students table may perform Full Table Scan

• enrollments table joined normally

• rows examined depends on current sample data

After indexes are added this plan should improve.
--------------------------------------------------------------
*/



-- ============================================================
-- TASK 2 : CREATE INDEXES
-- ============================================================

/*
Index on enrollment year

Useful because many reports filter students
based on admission year.
*/

CREATE INDEX idx_students_enrollment_year

ON students(enrollment_year);



/*
Composite UNIQUE index

Ensures one student cannot enroll
in the same course twice.
*/

CREATE UNIQUE INDEX idx_enrollment_unique

ON enrollments(student_id,course_id);



/*
Course lookup index
*/

CREATE INDEX idx_course_code

ON courses(course_code);



/*
MySQL does not support PostgreSQL style
partial indexes.

Instead, create a normal index.
*/

CREATE INDEX idx_grade

ON enrollments(grade);



/*
Run EXPLAIN again after indexing.
*/

EXPLAIN FORMAT=JSON

SELECT

s.first_name,

s.last_name,

c.course_name

FROM enrollments e

JOIN students s
ON s.student_id=e.student_id

JOIN courses c
ON c.course_id=e.course_id

WHERE s.enrollment_year=2022;



/*
------------------------------------------------------

Expected Observation

Before Index

students
↓

Full Table Scan

After Index

students
↓

Index Scan

This significantly reduces rows examined.

------------------------------------------------------
*/



/*
Test duplicate enrollment prevention.

This should fail because the UNIQUE
index prevents duplicate enrollments.
*/

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)

VALUES
(1,1,'2026-08-01','A');



-- ============================================================
-- VERIFY CREATED INDEXES
-- ============================================================

SHOW INDEX
FROM students;

SHOW INDEX
FROM enrollments;

SHOW INDEX
FROM courses;
