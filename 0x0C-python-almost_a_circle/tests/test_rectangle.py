#!/usr/bin/python3

"""Defines unittests for models/rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instantiantion(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class"""

    def test_rectangle_is_base(self):
        """Tests if rectangle is an intance of base"""

        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_no_arg(self):
        """Tests for no arg"""
        with self.assertRaises(Exception):
            Rectangle()

    def test_one_arg(self):
        """Tests or one arg"""

        with self.assertRaises(Exception):
            Rectangle(1)

    def test_two_args(self):
        """Tests two arg"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 3)
        self.assertEqual(r1.id,  r2.id -1)

    def test_three_args(self):
        """Tests for three args"""

        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(3, 4, 5)
        self.assertEqual(r1.id, r2.id -1)

    def test_four_args(self):
        """Tests for four args"""

        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, r2.id -1)

    def test_five_args(self):
        """Tests for five args"""

        self.assertEqual(1, Rectangle(10, 4, 5, 0, 1).id)

    def test_more_than_five_args(self):
        """Tests for more than five args"""

        with self.assertRaises(Exception):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_width(self):
        """Tests for private width"""

        with self.assertRaises(Exception):
             print(Rectangle(4, 5, 6).__width)

    def test_private_height(self):
        """Tests to private height"""

        with self.assertRaises(Exception):
            print(Rectangle(3, 7, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):

        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y) 


class TestRectangle_width(unittest.TestCase):
    """Unittest for testing initialization of Rectangle width attribute"""

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Ant", 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'a': 1}, 9)

    def test_list_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 9)

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1,), 5)

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 4)
    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1}, 4)

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(1), 5)

    def test_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1}), 9)

    def test_bytes(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytes("ALAreef", 'utf-8'), 1)

    def test_bytesarray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray("AlAreef", 'utf-8'), 9)

    def test_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'ABC'), 4)

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 8)

class TestRectangle_height(unittest.TestCase):
    """unittest for testing initialization of height attribute"""

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 2.5)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Ant")

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, {'a': 1})

    def test_list_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [1, 2])

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (1,))

    def test_boolean(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, True)
    def test_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, {1})

    def test_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(1))

    def test_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1}))

    def test_bytes(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, bytes("ALAreef", 'utf-8'))

    def test_bytesarray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, bytearray("AlAreef", 'utf-8'))

    def test_memoryview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, memoryview(b'ABC'))

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, float('inf'))

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, float('nan'))

    if __name__ == "__main__":
        unittest.main()
