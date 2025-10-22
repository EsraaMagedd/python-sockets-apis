from abc import ABC, abstractmethod

# ===== Abstract Base Class =====
class Person(ABC):
    def __init__(self, name, id):
        self._name = name
        self._id = id

    @abstractmethod
    def get_info(self):
        pass


# ===== Student Class (Inheritance from Person) =====
class Student(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.enrolled_courses = []

    def enroll(self, course):
        """Enroll the student in a course if not full."""
        if course.add_student(self):
            self.enrolled_courses.append(course)
            print(f"{self._name} enrolled in {course.name}")
        else:
            print(f"Cannot enroll {self._name} in {course.name} (Course full).")

    def get_info(self):
        """Return formatted info about the student."""
        return f"Student: {self._name} (ID: {self._id})"

    def __str__(self):
        courses = ', '.join([c.name for c in self.enrolled_courses]) or "None"
        return f"{self.get_info()}, Enrolled in: {courses}"


# ===== Course Class =====
class Course:
    def __init__(self, name, code, capacity):
        self.name = name
        self.code = code
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        """Add student if there is available capacity."""
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        return False

    def __str__(self):
        student_names = ', '.join([s._name for s in self.students]) or "No students"
        return f"Course: {self.name} ({self.code}) | Capacity: {self.capacity} | Students: {student_names}"


# ===== University Class (Aggregation) =====
class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def print_registration_report(self):
        print(f"\n📘 Registration Report — {self.name}")
        print("=" * 40)
        for course in self.courses:
            print(course)
        print("\nStudents Summary:")
        for student in self.students:
            print(student)


# ======== Main Execution (Testing) ========
if __name__ == "__main__":
    # Create university
    uni = University("Sadat University")

    # Create courses
    c1 = Course("Python Programming", "CS101", 2)
    c2 = Course("Data Structures", "CS201", 1)

    uni.add_course(c1)
    uni.add_course(c2)

    # Create students
    s1 = Student("Zahraa Gamal", "S001")
    s2 = Student("Dalia Ibrahim", "S002")
    s3 = Student("Amer Abdullah", "S003")
    s4 = Student("Mustafa Osama", "S004")

    uni.add_student(s1)
    uni.add_student(s2)
    uni.add_student(s3)
    uni.add_student(s4)

    # Enroll students
    s1.enroll(c1)
    s2.enroll(c1)
    s3.enroll(c1)   # This one should fail (course full)
    s3.enroll(c2)
    s4.enroll(c2)

    # Generate registration report
    uni.print_registration_report()
