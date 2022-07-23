import unittest
from gradebook import Person


class gradebookTest(unittest.TestCase):

    def update_first_name(self):
        john = Person('jack', 'smith','12/31/1990', 1)
        john.update_first_name('john')
        expected = 'john'
        actual = john.first_name()
        self.assertEqual(expected, actual)

    def update_last_name(self):
        doe = Person('jack', 'smith', '12/31/1990',1)
        doe.update_last_name('doe')
        expected = 'doe'
        actual = doe.last_name()
        self.assertEqual(expected, actual)

    def update_dob(self):
        birthdate = Person('jack', 'smith', '12/31/1990', 1)
        birthdate.update_dob('1/1/1991')
        expected = '1/1/1991'
        actual = birthdate.update_dob()
        self.assertEqual(expected, actual)

