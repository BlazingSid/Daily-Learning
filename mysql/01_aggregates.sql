CREATE TABLE students (
    id INTEGER,
    name TEXT,
    department TEXT,
    marks INTEGER
);

INSERT INTO students VALUES
(1, 'Shahid', 'AI', 92),
(2, 'Raj', 'AI', 85),
(3, 'Alex', 'CS', 78),
(4, 'Sam', 'CS', 88);

SELECT
    department,
    COUNT(*) AS students,
    AVG(marks) AS average_marks,
    MAX(marks) AS highest_marks
FROM students
GROUP BY department;