import unittest
import shapes

class shapeTest(unittest.TestCase):

    def test_is_Rectangle(self):
        length = 2
        width = 4
        expected_out = 8
        actual = shapes.Rectangle(length, width).area()
        self.assertEqual(expected_out, actual)

    def test_Square_area(self):
        side = 8
        expected_out = 64
        actual = shapes.Square(side).area()
        self.assertEqual(expected_out, actual)

    def test_Square_perimeter(self):
        side = 8
        expected_out = 32
        actual = shapes.Square(side).perimeter()
        self.assertEqual(expected_out, actual)

#         ]
# rect = shapes.Rectangle(2, 4)
# rect.area()
# # 8
#
# square = shapes.Square(8)
# square.area()
# # 64
#
# square.perimeter()
# # 32