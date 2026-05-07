import mysql.connector

def show_students():
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()

    print("\n 📚 Student Records:")
    for student in students:
        print(student)
    print("\n ✅ End of Records")


def add_student():

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    query = """
    INSERT INTO students (name, age, gender, course, marks)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, age, gender, course, marks)

    cursor.execute(query, values)
    conn.commit()

    print("✅ Student added successfully!")


def update_student():
    student_id = int(input("Enter Student ID to update: "))

    print("What do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Gender")
    print("4. Course")
    print("5. Marks")

    choice = input("Enter choice: ")

    if choice == '1':
        new_value = input("Enter new name: ")
        query = "UPDATE students SET name = %s WHERE student_id = %s"
    elif choice == '2':
        new_value = int(input("Enter new age: "))
        query = "UPDATE students SET age = %s WHERE student_id = %s"
    elif choice == '3':
        new_value = input("Enter new gender: ")
        query = "UPDATE students SET gender = %s WHERE student_id = %s"
    elif choice == '4':
        new_value = input("Enter new course: ")
        query = "UPDATE students SET course = %s WHERE student_id = %s"
    elif choice == '5':
        new_value = float(input("Enter new marks: "))
        query = "UPDATE students SET marks = %s WHERE student_id = %s"
    else:
        print("Invalid choice")
        return

    cursor.execute(query, (new_value, student_id))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ Student ID not found.")
    else:
        print("✅ Student updated successfully!")


def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    # Optional: confirm before deleting
    confirm = input("Are you sure? (yes/no): ").lower()
    if confirm != 'yes':
        print("Deletion cancelled.")
        return

    query = "DELETE FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ Student ID not found.")
    else:
        print("✅ Student deleted successfully!")

def search_student():
    print("\nSearch by:")
    print("1. Name")
    print("2. Course")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name to search: ")
        query = "SELECT * FROM students WHERE name LIKE %s"
        value = ('%' + name + '%',)

    elif choice == '2':
        course = input("Enter course to search: ")
        query = "SELECT * FROM students WHERE course LIKE %s"
        value = ('%' + course + '%',)

    else:
        print("Invalid choice")
        return

    cursor.execute(query, value)
    records = cursor.fetchall()

    if len(records) == 0:
        print("❌ No matching records found.")
    else:
        print("\n--- Search Results ---")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Course: {row[4]}, Marks: {row[5]}")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Syam@9500",
    database="students_DB"
)

cursor = conn.cursor()

print("Welcome to the Student Management System!\n")

print("\n===== Student Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Update Student")
print("4. Delete Student")
print("5. Search Student")
print("6. Exit")
option = int(input("\n Enter the Option: "))

if option == 1:
    add_student()

elif option == 2:
    show_students()
    
elif option == 3:
    update_student()
    print("\n Updated Student Records:")
    show_students()

elif option == 4:
    delete_student()
    print("\n Updated Student Records:")
    show_students()

elif option == 5:
    search_student()

elif option == 6:
    print("\n Exiting...")

else:
    print("\n Invalid choice, try again.")

print("\n Thank you for using the Student Management System!\n")


conn.close()