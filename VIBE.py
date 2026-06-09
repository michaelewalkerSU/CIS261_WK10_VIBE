#Michael E Walker
#CIS261
#WK10 VIBE Coding - Student Grade Calculator

# Student class stores name, ID, three test scores, average, and grade.
class Student:
    def __init__(self, name, student_id, test1, test2, test3):
        self.name = name
        self.student_id = student_id
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.average = (test1 + test2 + test3) / 3
        self.grade = self._calculate_letter_grade()

    # Determine the letter grade from the average score.
    def _calculate_letter_grade(self):
        if self.average >= 90:
            return "A"
        if self.average >= 80:
            return "B"
        if self.average >= 70:
            return "C"
        if self.average >= 60:
            return "D"
        return "F"

    # Convert the student record into a pipe-delimited string for file storage.
    def to_file_string(self):
        return (
            f"{self.name}|{self.student_id}|{self.test1:.2f}|{self.test2:.2f}|"
            f"{self.test3:.2f}|{self.average:.2f}|{self.grade}"
        )

def banner():
    print(f"{'='*50}")

# Prompt the user for a floating-point score and re-prompt until valid.
def prompt_float(prompt_text):
    while True:
        user_input = input(prompt_text).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number for the score.")

# Add a new student to the list and show a confirmation line.
def add_new_student(students):
    print()
    banner()
    print("Add New Student")
    banner()
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()
    test1 = prompt_float("Enter Test 1 score: ")
    test2 = prompt_float("Enter Test 2 score: ")
    test3 = prompt_float("Enter Test 3 score: ")
    student = Student(name, student_id, test1, test2, test3)
    students.append(student)
    print(
        f"Student added: {student.name} | ID: {student.student_id}\n"
        f"Average: {student.average:.2f} | Grade: {student.grade}\n"
    )

# Display all students in a formatted table with aligned columns.
def display_all_students(students):
    print()
    banner()
    print("Display All Students")
    banner()
    if not students:
        print("No students available. Add students first.\n")
        return

    name_width = max(len(student.name) for student in students)
    id_width = max(len(student.student_id) for student in students)
    name_width = max(name_width, len("Name"))
    id_width = max(id_width, len("ID"))

    header = (
        f"{ 'Name':<{name_width}}  { 'ID':<{id_width}}  "
        f"{'Test 1':>6}  {'Test 2':>6}  {'Test 3':>6}  {'Average':>7}  {'Grade':>5}"
    )
    print(header)
    print("-" * len(header))
    for student in students:
        print(
            f"{student.name:<{name_width}}  {student.student_id:<{id_width}}  "
            f"{student.test1:6.2f}  {student.test2:6.2f}  {student.test3:6.2f}  "
            f"{student.average:7.2f}  {student.grade:>5}"
        )
    print(f"\nTotal students: {len(students)}\n")

# Search for a student by name case-insensitively and show details.
def search_student_by_name(students):
    print()
    banner()
    print("Search Student by Name")
    banner()
    if not students:
        print("No students available to search.\n")
        return
    search_name = input("Enter the student name to search for: ").strip().lower()
    found = [s for s in students if s.name.lower() == search_name]
    if not found:
        print("No student found with that name.\n")
        return

    print("Student found:")
    for student in found:
        print(
            f"Name: {student.name}\n"
            f"ID: {student.student_id}\n"
            f"Test 1: {student.test1:.2f}\n"
            f"Test 2: {student.test2:.2f}\n"
            f"Test 3: {student.test3:.2f}\n"
            f"Average: {student.average:.2f}\n"
            f"Grade: {student.grade}\n"
        )

# Show class statistics including class average, highest, lowest, and letter distribution.
def view_class_statistics(students):
    print()
    banner()
    print("View Class Statistics")
    banner()
    if not students:
        print("No students available for statistics.\n")
        return

    averages = [student.average for student in students]
    class_average = sum(averages) / len(averages)
    highest = max(students, key=lambda s: s.average)
    lowest = min(students, key=lambda s: s.average)

    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student in students:
        distribution[student.grade] += 1

    print(f"Class average: {class_average:.2f}")
    print(f"Highest average: {highest.average:.2f} ({highest.name})")
    print(f"Lowest average: {lowest.average:.2f} ({lowest.name})")
    print("Grade distribution:")
    print(f"  A: {distribution['A']}")
    print(f"  B: {distribution['B']}")
    print(f"  C: {distribution['C']}")
    print(f"  D: {distribution['D']}")
    print(f"  F: {distribution['F']}\n")

# Save all students to a file using the Student.to_file_string format.
def save_students_to_file(students, filename="student_grades.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for student in students:
                file.write(student.to_file_string() + "\n")
        print(f"Students saved successfully to {filename}.\n")
    except Exception as error:
        print(f"Error saving students to file: {error}\n")

# Load students from a file if it exists, and return the loaded list.
def load_students_from_file(filename="student_grades.txt"):
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) < 5:
                    continue
                name, student_id, test1_str, test2_str, test3_str = parts[:5]
                try:
                    test1 = float(test1_str)
                    test2 = float(test2_str)
                    test3 = float(test3_str)
                    students.append(Student(name, student_id, test1, test2, test3))
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    return students

# Print the menu options to the user.
def print_menu():
    banner()
    print("STUDENT GRADE CALCULATOR")
    banner()
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. View Class Statistics")
    print("5. Save and Exit (or press ESC)")

# Main loop for the program, loading data first and then handling menu selections.
def main():
    students = load_students_from_file()
    if students:
        print(f"Loaded {len(students)} student(s) from student_grades.txt.\n")
    else:
        print("No saved student data found. Starting with an empty list.\n")

    print_menu()
    while True:
        selection = input("Select an option (1-5) or press ESC to exit: ")
        if chr(27) in selection:
            save_students_to_file(students)
            break

        if selection == "1":
            add_new_student(students)
        elif selection == "2":
            display_all_students(students)
        elif selection == "3":
            search_student_by_name(students)
        elif selection == "4":
            view_class_statistics(students)
        elif selection == "5":
            save_students_to_file(students)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5 or press ESC to exit.\n")

if __name__ == "__main__":
    main()
