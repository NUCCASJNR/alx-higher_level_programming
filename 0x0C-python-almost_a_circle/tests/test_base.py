#!/usr/bin/python3
"""Unittests for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """unittests for testing instantiation of the Base class"""

    def test_no_arg(self):
        """Tests for no arg"""
        
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_three_bases(self):
        """Tests for three args"""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id -2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id) 

    def  test_negative_int_id(self):
        self.assertEqual(-10, Base(-10).id)

    def test_float_id(self):
        self.assertEqual(3.2, Base(3.2).id)

    def test_negative_float_id(self):
        self.assertEqual(-3.2, Base(-3.2).id)

    def test_list_id(self):
        self.assertEqual({"a": 1}, Base({"a": 1}).id)

    def test_exception_id(self):
        with self.assertRaises(Exception):
            ((1, 2), Base(1, 2).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_set_id(self):
        self.assertEqual({1, 2}, Base({1, 2}).id)

    def test_complex_id(self):
        self.assertEqual(complex(1), Base(complex(1)).id) 

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2}), Base(frozenset({1, 2})).id)

    def test_range_id(self):
        self.assertEqual(range(2), Base(range(2)).id)

    def test_str_id(self):
        self.assertEqual(str("AlAreef"), Base(str("AlAreef")).id)

    def test_bytes_id(self):
        self.assertEqual(bytes(b"AlAreef"),  Base(bytes(b"AlAreef")).id)

    def test_bytesarray_id(self):
        self.assertEqual(bytearray("AlAreef", 'utf-8'), Base(bytearray("AlAreef", 'utf-8')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'ABC'), Base(memoryview(b'ABC')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(Exception):
            Base(1, 2)

    if __name__ == "__main__":
        unittest.main()
