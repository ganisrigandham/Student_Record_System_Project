class StudentRecordSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")
        marks = float(input("Enter Marks: "))

        self.students[roll_no] = {
            "name": name,
            "branch": branch,
            "marks": marks
        }

        print("Student added successfully!")

    def search_student(self):
        roll_no = input("Enter Roll Number to search: ")

        if roll_no in self.students:
            student = self.students[roll_no]
            print("\nStudent Details")
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Marks:", student["marks"])
        else:
            print("Student not found.")

    def display_students(self):
        if not self.students:
            print("No student records available.")
            return

        print("\n===== Student Records =====")

        for roll_no, student in self.students.items():
            print("Roll Number:", roll_no)
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Marks:", student["marks"])
            print("--------------------------")


system = StudentRecordSystem()

while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.search_student()

    elif choice == "3":
        system.display_students()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")