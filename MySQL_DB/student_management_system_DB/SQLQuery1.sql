
CREATE DATABASE student_DB;

use student_DB;


CREATE TABLE students (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    course VARCHAR(100),
    marks FLOAT
);


Describe students_DB; 