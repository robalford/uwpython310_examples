# Example program for tracking a class of student's grades and creating grade reports

class Assignment:
    total_possible_points = 100

    def __init__(self, assignment_number, points_earned):
        self.assignment_number = assignment_number
        self.points_earned = points_earned

    def __str__(self):
        return (f"Assignment number: {self.assignment_number} "
                f"\nPoints earned: {self.points_earned}/{self.total_possible_points} "
                f"\nGrade point value: {self.grade_point_value}")

    def __repr__(self):
        return f"Assignment({self.assignment_number}, {self.points_earned})"

    @property
    def grade_point_value(self):
        """Calculate grade point value from points earned."""
        grade_point_value = (self.points_earned / self.total_possible_points) * 4.0
        return round(grade_point_value, 1)

    @classmethod
    def from_grade_point_value(cls, assignment_number, grade_point_value):
        """Alternative initializer method for creating Assignment instance from grade point value."""
        points_earned = (grade_point_value / 4.0) * cls.total_possible_points
        return cls(assignment_number, int(points_earned))


class Student:
    def __init__(self, name):
        self.name = name
        self.assignments = []

    def __str__(self):
        """String representation used to create a tabular row for use in grade report."""
        name = f"{self.name:<10} | "
        student_grades = " | ".join([str(assignment.grade_point_value) for assignment in self.assignments])
        total_grade = f" | GPA: {self.grade_point_average:<5} | Grade: {self.letter_grade}"
        return name + student_grades + total_grade

    def __repr__(self):
        return f"Student({self.name})"

    def __lt__(self, other):
        """Sort instance objects by grade_point_average value."""
        return self.grade_point_average < other.grade_point_average

    def grade_assignment(self, assignment):
        self.assignments.append(assignment)

    @property
    def grade_point_average(self):
        """Calculate total grade point average across all assignments."""
        total_grade_points = sum([assignment.grade_point_value for assignment in self.assignments])
        grade_point_average = total_grade_points / len(self.assignments)
        return round(grade_point_average, 1)

    @property
    def letter_grade(self):
        """Determine letter grade from grade_point_average."""
        if self.grade_point_average < 2.4:
            return 'F'
        elif self.grade_point_average < 2.8:
            return 'D'
        elif self.grade_point_average < 3.2:
            return 'C'
        elif self.grade_point_average < 3.6:
            return 'B'
        return 'A'


# This code is here to simulate grade submissions for students and give us some data
# to generate our grade report

students_and_grades = {
    "Rob": [4.0, 90, 80, 70, 60],
    "Tara": [99, 99, 99, 99, 99],
    "Zoe": [80, 90, 80, 90, 4.0],
    "Max": [90, 4.0, 90, 4.0, 90],
    "Julie": [80, 81, 82, 83, 84],
    "Nick": [90, 92, 94, 96, 98],
    "Lowell": [30, 60, 90, 60, 30],
}

all_students = []

for student_name, grades in students_and_grades.items():
    new_student = Student(student_name)
    for i, grade in enumerate(grades, start=1):
        if type(grade) is float:
            new_student.grade_assignment(Assignment.from_grade_point_value(i, grade))
        else:
            new_student.grade_assignment(Assignment(i, grade))
    all_students.append(new_student)


def student_report(student):
    print(f"Grade report for {student.name}")
    for assignment in student.assignments:
        print("----------------------")
        print(assignment)
    print("----------------------")
    print(f"Total GPA: {student.grade_point_average}")
    print(f"Total grade: {student.letter_grade}")


# student_report(all_students[0])
# student_report(all_students[-1])


def class_report(students):
    print("Class Grade Report")
    print("----------------------------------------------------------------")
    for student in sorted(students, reverse=True):
        print(student)


# class_report(all_students)
