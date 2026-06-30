/*==========================================================
 HANDS-ON 3
 Advanced SQL - Subqueries, Views & Transactions

 Scenario:
 Student Course Registration System

 Author : Mohammed Thoufik
==========================================================*/


/*==========================================================
TASK 1 - SUBQUERIES
==========================================================*/


/*----------------------------------------------------------
Query 1
Find students enrolled in more courses than the average
number of enrollments per student.
----------------------------------------------------------*/

SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    COUNT(e.course_id) AS total_courses
FROM Students s
JOIN Enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id,s.first_name,s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(course_id) AS course_count
        FROM Enrollments
        GROUP BY student_id
    ) AS avg_table
);



/*----------------------------------------------------------
Query 2
Find courses where every enrolled student has received
grade 'A'.

NOT EXISTS is used to make sure there are no students
with grades other than A.
----------------------------------------------------------*/

SELECT
    c.course_id,
    c.course_name
FROM Courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM Enrollments e
    WHERE e.course_id = c.course_id
    AND e.grade <> 'A'
);



/*----------------------------------------------------------
Query 3

Find the highest paid professor in every department.

Uses a correlated subquery because each department is
checked individually.
----------------------------------------------------------*/

SELECT
    p.professor_id,
    p.professor_name,
    p.department_id,
    p.salary
FROM Professors p
WHERE salary =
(
    SELECT MAX(p2.salary)
    FROM Professors p2
    WHERE p2.department_id = p.department_id
);



/*----------------------------------------------------------
Query 4

Derived Table Example

Calculate average salary of every department and display
only departments whose average salary exceeds 85000.
----------------------------------------------------------*/

SELECT *
FROM
(
    SELECT
        department_id,
        AVG(salary) AS average_salary
    FROM Professors
    GROUP BY department_id
) AS department_average
WHERE average_salary > 85000;



/*==========================================================
TASK 2
CREATING AND USING VIEWS
==========================================================*/


/*----------------------------------------------------------
View 1

Student Enrollment Summary

Displays:
Student Name
Department
Total Courses
GPA
----------------------------------------------------------*/

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.department_name,

    COUNT(e.course_id) AS total_courses,

    AVG(
        CASE
            WHEN e.grade='A' THEN 4
            WHEN e.grade='B' THEN 3
            WHEN e.grade='C' THEN 2
            WHEN e.grade='D' THEN 1
            ELSE 0
        END
    ) AS GPA

FROM Students s

JOIN Departments d
ON s.department_id=d.department_id

LEFT JOIN Enrollments e
ON s.student_id=e.student_id

GROUP BY
s.student_id,
student_name,
department_name;



/*----------------------------------------------------------
View 2

Course Statistics
----------------------------------------------------------*/

CREATE VIEW vw_course_stats AS

SELECT

c.course_name,
c.course_code,

COUNT(e.student_id) AS total_enrollments,

AVG(
CASE
WHEN e.grade='A' THEN 4
WHEN e.grade='B' THEN 3
WHEN e.grade='C' THEN 2
WHEN e.grade='D' THEN 1
ELSE 0
END
) AS avg_gpa

FROM Courses c

LEFT JOIN Enrollments e
ON c.course_id=e.course_id

GROUP BY
c.course_name,
c.course_code;



/*----------------------------------------------------------
Display students having GPA above 3
----------------------------------------------------------*/

SELECT *
FROM vw_student_enrollment_summary
WHERE GPA > 3;



/*----------------------------------------------------------
Attempt to update through the view

This will fail because the view is built using
multiple joined tables.

Multi-table views are generally not updatable.
----------------------------------------------------------*/

UPDATE vw_student_enrollment_summary
SET student_name='Test Student'
WHERE student_id=1;



/*----------------------------------------------------------
Drop the views
----------------------------------------------------------*/

DROP VIEW vw_course_stats;

DROP VIEW vw_student_enrollment_summary;



/*----------------------------------------------------------
Recreate a simple updatable view

WITH CHECK OPTION prevents updates that violate
the view condition.
----------------------------------------------------------*/

CREATE VIEW vw_student_enrollment_summary AS

SELECT
student_id,
first_name,
last_name,
department_id

FROM Students

WHERE department_id=1

WITH CHECK OPTION;



/*==========================================================
TASK 3
STORED PROCEDURES & TRANSACTIONS
==========================================================*/


/*----------------------------------------------------------
Stored Procedure

Enroll a student only if the enrollment does not
already exist.
----------------------------------------------------------*/

DELIMITER $$

CREATE PROCEDURE sp_enroll_student
(
IN p_student_id INT,
IN p_course_id INT,
IN p_enrollment_date DATE
)

BEGIN

IF EXISTS
(
SELECT *
FROM Enrollments
WHERE student_id=p_student_id
AND course_id=p_course_id
)

THEN

SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT='Student already enrolled in this course';

ELSE

INSERT INTO Enrollments
(student_id,course_id,enrollment_date)

VALUES
(p_student_id,p_course_id,p_enrollment_date);

END IF;

END $$

DELIMITER ;



/*----------------------------------------------------------
Create log table for department transfers
----------------------------------------------------------*/

CREATE TABLE department_transfer_log
(
log_id INT AUTO_INCREMENT PRIMARY KEY,

student_id INT,

old_department INT,

new_department INT,

transfer_date DATETIME
);



/*----------------------------------------------------------
Procedure to transfer student
----------------------------------------------------------*/

DELIMITER $$

CREATE PROCEDURE sp_transfer_student
(

IN p_student INT,

IN p_new_department INT

)

BEGIN

DECLARE old_department INT;

START TRANSACTION;

SELECT department_id
INTO old_department
FROM Students
WHERE student_id=p_student;

UPDATE Students

SET department_id=p_new_department

WHERE student_id=p_student;

INSERT INTO department_transfer_log

(

student_id,
old_department,
new_department,
transfer_date

)

VALUES

(

p_student,
old_department,
p_new_department,
NOW()

);

COMMIT;

END $$

DELIMITER ;



/*----------------------------------------------------------
Transaction Rollback Example
----------------------------------------------------------*/

START TRANSACTION;

UPDATE Students

SET department_id=2

WHERE student_id=1;

/*
Deliberately using an invalid foreign key to simulate
an error.
*/

INSERT INTO department_transfer_log

(

student_id,
old_department,
new_department,
transfer_date

)

VALUES

(

9999,
1,
2,
NOW()

);

ROLLBACK;



/*----------------------------------------------------------
SAVEPOINT Example
----------------------------------------------------------*/

START TRANSACTION;

INSERT INTO Enrollments
VALUES
(1001,2,3,'2026-07-01','A');

SAVEPOINT first_insert;

INSERT INTO Enrollments
VALUES
(9999,5,2,'2026-07-02','B');

/*
If second insert fails,
return only to the savepoint.
*/

ROLLBACK TO first_insert;

COMMIT;