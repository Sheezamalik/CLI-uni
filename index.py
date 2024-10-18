import random

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.teachers = []
        self.students = []

    def add_department(self, department, silent=False):
        self.departments.append(department)
        if not silent:
            print(f"Department '{department}' added.")

    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
            print(f"Department '{department}' removed.")
        else:
            print(f"Department '{department}' not found.")

    def get_departments(self):
        print("Departments:")
        for dept in self.departments:
            print(dept)

    def add_teacher(self, teacher, silent=False):
        self.teachers.append(teacher)
        if not silent:
            print(f"Teacher {teacher.name} added.")

    def get_teachers(self):
        print("Teachers:")
        for teacher in self.teachers:
            print(teacher.name)

    def add_student(self, student, silent=False):
        self.students.append(student)
        if not silent:
            print(f"Student '{student.name}' added.")

class Person:
    def __init__(self, name, age, contact, role):
        self.name = name
        self.age = age
        self.contact = contact
        self.role = role

class Teacher(Person):
    def __init__(self, name, age, contact, role, departments):
        super().__init__(name, age, contact, role)
        self.departments = departments
        self.requests = []

    def view_requests(self):
        if self.requests:
            print("\nRequests from students:")
            for i, request in enumerate(self.requests, 1):
                print(f"{i}. Request from {request[0]}: {request[1]}")
        else:
            print("No requests from students.")

    def view_schedule(self):
        print("Class Schedule:")
        print("Tuesday: 10 AM - 12 PM")
        print("Thursday: 1 PM - 3 PM")

    def approve_request(self, request_number):
        if 0 < request_number <= len(self.requests):
            student_name, message = self.requests[request_number - 1]
            print(f"Request '{message}' from {student_name} approved.")
            self.requests.pop(request_number - 1)
        else:
            print("Invalid request number.")

class Student(Person):
    def __init__(self, name, age, contact, role, department, semester, courses):
        super().__init__(name, age, contact, role)
        self.department = department
        self.semester = semester
        self.courses = courses
        self.requests = []

    def raise_request(self, teacher, message):
        teacher.requests.append((self.name, message))
        self.requests.append(message)
        print(f"Request raised to {teacher.name}: {message}")

    def show_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Semester: {self.semester}")
        print(f"Courses: {', '.join(self.courses)}")

class Admin(Person):
    def __init__(self, name, age, contact, role):
        super().__init__(name, age, contact, role)

    def add_teacher(self, university):
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        contact = input("Enter teacher contact: ")
        department = input("Enter department for the teacher: ")

        if department in university.departments:
            new_teacher = Teacher(name, age, contact, "Teacher", [department])
            university.add_teacher(new_teacher)
            print(f"Teacher {name} added to department {department}.")
        else:
            print(f"Department '{department}' not found. Please add the department first.")

# Function to generate a random student
def generate_random_student():
    names = ["Ali", "Sara", "Hassan", "Fatima", "Zain", "Ayesha", "Ahmed", "Noor", "Usman", "Zara"]
    departments = ["Computer Science", "Artificial Intelligence", "Data Science"]
    courses = ["AI", "ML", "Data Science", "Software Engineering"]
    
    name = random.choice(names)
    age = random.randint(20, 25)
    contact = f"555{random.randint(1000000, 9999999)}"
    department = random.choice(departments)
    semester = f"Semester {random.randint(1, 8)}"
    selected_courses = random.sample(courses, 2)

    return Student(name, age, contact, "Student", department, semester, selected_courses)

def main():
    university = University("PIAIC (Presidential Initiative for Artificial Intelligence & Computing)")
    university.add_department("Computer Science", silent=True)
    university.add_department("Artificial Intelligence", silent=True)

    teacher1 = Teacher("Jhanzaib", 28, "5551234567", "Teacher", ["Data Science"])
    teacher2 = Teacher("Amna", 27, "5559876543", "Teacher", ["Data Science"])

    university.add_teacher(teacher1, silent=True)
    university.add_teacher(teacher2, silent=True)

    # Add 4 random students without printing messages
    for _ in range(4):
        university.add_student(generate_random_student(), silent=True)

    while True:
        print("\nWelcome to PIAIC\n")
        print("Select your role:")
        print("1. Admin")
        print("2. Teacher")
        print("3. Student")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print("You are an Admin!")
            admin = Admin("Zia Khan", 51, "5555555555", "Admin")
            while True:
                print("\nAdmin Options:")
                print("1. View Departments")
                print("2. Add Department")
                print("3. Remove Department")
                print("4. Add Teacher")
                print("5. Add Student")
                print("6. Exit")

                admin_choice = input("Enter your choice: ")

                if admin_choice == '1':
                    university.get_departments()
                elif admin_choice == '2':
                    dept_name = input("Enter the name of the department to add: ")
                    university.add_department(dept_name)
                elif admin_choice == '3':
                    dept_name = input("Enter the name of the department to remove: ")
                    university.remove_department(dept_name)
                elif admin_choice == '4':
                    admin.add_teacher(university)
                elif admin_choice == '5':
                    student_name = input("Enter student name: ")
                    for student in university.students:
                        if student.name == student_name:
                            print("Student already exists!")
                            break
                    else:
                        new_student = generate_random_student()
                        university.add_student(new_student)
                elif admin_choice == '6':
                    break
                else:
                    print("Invalid choice!")

        elif choice == '2':
            teacher_name = input("Enter teacher name (Jhanzaib, Amna): ")
            for teacher in university.teachers:
                if teacher.name == teacher_name:
                    print(f"Welcome {teacher.name}!")
                    while True:
                        print("\nTeacher Options:")
                        print("1. View Departments")
                        print("2. View Class Schedule")
                        print("3. View Requests")
                        print("4. Exit")

                        teacher_choice = input("Enter your choice (1/2/3/4): ")

                        if teacher_choice == '1':
                            print(f"Departments: {', '.join(teacher.departments)}")
                        elif teacher_choice == '2':
                            teacher.view_schedule()
                        elif teacher_choice == '3':
                            teacher.view_requests()
                            if teacher.requests:
                                request_choice = int(input("Enter the request number to approve: "))
                                teacher.approve_request(request_choice)
                        elif teacher_choice == '4':
                            break
                        else:
                            print("Invalid choice!")
                    break
            else:
                print("Teacher not found.")

        elif choice == '3':
            print("You are a Student!")
            student_name = input("Enter student name: ")
            for student in university.students:
                if student.name == student_name:
                    print(f"Welcome {student.name}!")
                    while True:
                        print("\nStudent Options:")
                        print("1. View Student Details")
                        print("2. View Class Timings")
                        print("3. Raise a Request")
                        print("4. Exit")

                        student_choice = input("Enter your choice (1/2/3/4): ")

                        if student_choice == '1':
                            student.show_student_info()
                        elif student_choice == '2':
                            student.view_class_timings(university)
                        elif student_choice == '3':
                            teacher_name = input("Enter teacher name to raise request to: ")
                            message = input("Enter your message: ")
                            for teacher in university.teachers:
                                if teacher.name == teacher_name:
                                    student.raise_request(teacher, message)
                                    break
                            else:
                                print("Teacher not found.")
                        elif student_choice == '4':
                            break
                        else:
                            print("Invalid choice!")
                    break
            else:
                print("Student not found.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

university = University("PIAIC (Presidential Initiative for Artificial Intelligence & Computing)")
main()
