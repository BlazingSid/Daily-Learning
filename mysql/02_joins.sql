CREATE TABLE students (
    id INTEGER,
    name TEXT
);

CREATE TABLE courses (
    student_id INTEGER,
    course TEXT
);

INSERT INTO students VALUES
(1, 'Shahid'),
(2, 'Raj'),
(3, 'Alex');

INSERT INTO courses VALUES
(1, 'Machine Learning'),
(2, 'Python'),
(3, 'Database Systems');

SELECT
    students.name,
    courses.course
FROM students
INNER JOIN courses
ON students.id = courses.student_id;