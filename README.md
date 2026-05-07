# Student Management System 📚


A simple Student Management System built using Python and MySQL.
This project allows users to perform basic CRUD operations such as adding, viewing, updating, deleting, and searching student records.

### 🚀 Features
- Add new student records
- View all students
- Update existing student details
- Delete student records
- Search students by:

-> Name
  
-> Course
  
- MySQL database integration
- Simple command-line interface (CLI)

### 🛠️ Technologies Used
- Python
- MySQL
- MySQL Connector for Python

### 📂 Project Structure
`Student-Management-System/`

`│`

`├── DB_Connect.py              # Main Python file`

`├── student_management_system_project.sql   # MySQL database file`

`└── README.md`

### ⚙️ Database Setup
1) Open MySQL.

2) Create a database:

`CREATE DATABASE students_DB;`


3) Import the SQL file:


`USE students_DB;`

`SOURCE student_management_system_project.sql;`

### ▶️ How to Run the Project
- Step 1: Install MySQL Connector
- 
`pip install mysql-connector-python`

- Step 2: Update Database Credentials
  
Inside DB_Connect.py, update:

`conn = mysql.connector.connect(   
host="localhost",    
user="root",    
password="your_password",   
database="students_DB")`

- Step 3: Run the Program
  
`python DB_Connect.py`

### 📸 Menu Options
===== Student Management System =====
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit

### 📌 Example Functionalities

- ✅ Add Student
  
Stores student details like:
Name
Age
Gender
Course
Marks


✅ Update Student
Modify:


Name


Age


Gender


Course


Marks


✅ Search Student
Search records using:


Student Name


Course Name



🔮 Future Improvements


GUI using Tkinter


Login Authentication


Export records to Excel/CSV


Multiple user support


Better exception handling



👨‍💻 Author
Syam Prasanth

📄 License
This project is for learning and educational purposes.
