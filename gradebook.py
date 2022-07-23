from enum import Enum

class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1

class Person():
    def __init__(self,first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, alive):
        self.alive = alive


class Instructor(Person):
# This class must inherit from the Person class.
# This class must have an additional attribute called instructor_id.
# The instructor_id attribute must start with the string "Instructor_" followed by a UUID value.
# Hint: Use super class calls.

pass


class Student(Person):
# This class must inherit from the Person class.
# This class must have an additional attribute called student_id.
# The student_id attribute must start with the string "Student_" followed by a UUID value.

pass


class ZipCodeStudent(Student):
# This class must inherit from the Student class.

pass

class PreK(Student):
# This class must inherit from the Student class.

pass

class Classroom():
# Classroom class must have the following attributes:
#
# students - a container for students
# instructors - a container for instructors
# Classroom class must also have the following methods:
#
# add_instructor
# remove_instructor
# add_student
# remove_student
# print_instructors
# print_students

pass