

class Grades(object):
    """Maping from students to a list grades"""
    def __init__(self):
        self.students = []  # list of students objects
        self.grades = {}    # maps idNum -> list of grades
        self.isSorted = True

    def addStudent(self, student):
        if student in self.students:
            raise ValueError("Duplicate student!")
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Add grade to the list of grades for student."""
        try:
            self.grades[student.getIdNum()].append(grade
        except KeyError:
            raise ValueError("Student not in grade book.")

    def getGrades(self, student):
        """Return a list of grades for a student."""
        try:                # return a copy of a student grades
            self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError("Student not in grade book.")

    def allStudents(self):
        """Return a list of students in the grade book."""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s   