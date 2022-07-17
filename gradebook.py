from enum import Enum

class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1

class Person():
# Person class must have the following attributes:
#
# first_name
# last_name
# dob (date of birth)
# alive (of type AliveStatus)
# Person class must also have the following methods:
#
# update_first_name
# update_last_name
# update_dob
# update_status

pass

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