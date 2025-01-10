# write a program that stores student data in a dictionary and performs crud operations 
students = {}

# Function to add a student
def add_student(student_id, name, age, grades):
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
    else:
        students[student_id] = {'Name': name, 'Age': age, 'Grades': grades}
        print(f"Student {name} added successfully.")

# Function to view a student's details
def view_student(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"ID: {student_id}, Name: {student['Name']}, Age: {student['Age']}, Grades: {student['Grades']}")
    else:
        print(f"Student with ID {student_id} not found.")

# Function to update a student's details
def update_student(student_id, name=None, age=None, grades=None):
    if student_id in students:
        if name:
            students[student_id]['Name'] = name
        if age:
            students[student_id]['Age'] = age
        if grades:
            students[student_id]['Grades'] = grades
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"Student with ID {student_id} not found.")

# Function to delete a student
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"Student with ID {student_id} not found.")

# Main program loop
def main():
    while True:
        print("\nStudent Data Management")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grades = list(map(float, input("Enter Grades (comma-separated): ").split(',')))
            add_student(student_id, name, age, grades)
        elif choice == '2':
            student_id = input("Enter Student ID to view: ")
            view_student(student_id)
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            print("Leave fields blank if you don't want to update them.")
            name = input("Enter Name: ") or None
            age = input("Enter Age: ")
            age = int(age) if age else None
            grades = input("Enter Grades (comma-separated): ")
            grades = list(map(float, grades.split(','))) if grades else None
            update_student(student_id, name, age, grades)
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            if students:
                for student_id, details in students.items():
                    print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grades: {details['Grades']}")
            else:
                print("No students found.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
