
CREATE DATABASE students_DB;

USE students_DB;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    course VARCHAR(100),
    marks FLOAT
);

DESCRIBE students;

SHOW Tables;

INSERT INTO students (name, age, gender, course, marks)
VALUES 
('Rahul', 20, 'Male', 'BCA', 85),
('Anjali', 21, 'Female', 'BBA', 90);

select * from students;

