from enum import Enum
from uuid import uuid4

class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1

class Person():
    def __init__(self,first_name, last_name, dob, AliveStatus):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus

    def update_first_name(self, first_name):
        self.first_name = first_name
        return first_name

    def update_last_name(self, last_name):
        self.last_name = last_name
        return last_name

    def update_dob(self, dob):
        self.dob = dob
        return dob

    def update_status(self, status):
        self.alive = status


class Instructor(Person):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name,last_name,dob)

        self.instructor_id = (f'Instructor_{uuid4()}')


# This class must inherit from the Person class.
# This class must have an additional attribute called instructor_id.
# The instructor_id attribute must start with the string "Instructor_" followed by a UUID value.
# Hint: Use super class calls.




class Student(Person):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)

        self.student_id = (f'Student_{uuid4()})

# This class must inherit from the Person class.
# This class must have an additional attribute called student_id.
# The student_id attribute must start with the string "Student_" followed by a UUID value.


class ZipCodeStudent(Student):
     def __init__(self, first_name, last_name, dob):
         super().__init__(first_name, last_name, dob)

# This class must inherit from the Student class.



class PreK(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)

# This class must inherit from the Student class.



class Classroom():
# Classroom class must have the following attributes:
#
# students - a container for students
# instructors - a container for instructors

    students = []
    instructors = []

# Classroom class must also have the following methods:
#
# add_instructor
# remove_instructor
# add_student
# remove_student
# print_instructors
# print_students
    def add_instructor(self, instructor):
        self.instructors.append(Instructor)
        return self.instructors

    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)
        return self.instructors

    def add_student(self, student):
        self.students.appen(student)
        return self.students

    def remove_student(self, student):
        self.students.remove(student)
        return self.students

    def print_instructors(self):
        print(self.instructors)

    def print_students(self):
        print(self.students)
