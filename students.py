class Student:
    def __init__(self, name, age, grades):

        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0
if __name__ == "__main__":
    student = Student(name="John Doe", age=20, grades=[85, 90, 78])
    student.display_details()
    avg = student.calculate_average()
    print(f"Average Grade: {avg:.2f}")
