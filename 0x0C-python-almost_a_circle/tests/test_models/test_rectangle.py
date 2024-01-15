#!/usr/bin/python3
"""Unittest for rectangle.py"""
import unittest
import sys
import io
from io import StringID
from models.basr import Base
from models.rectangle import Rectangle


class TestRectangle_instiattion(unittest.Testcase):
    """testing instaition of the rectagle class"""

    def test_class(self):
        """testing increment of object id"""
        rect_test1 = Rectangle(2, 3, 2, 2)
        self.assertTrue(type(rect_test1) is Rectangle and issubclass(Rectangle, Base))
        rect_test2 = Rectangle(2,5, 3, 4)
        self.assertisinstance(rect_test2, rectangle)

    def test_val(self):
        """checks for valid value input"""
        rect_test1 = Rectangle(8, 2)
        rect_test2 = Rectangle(3, 7)
        self. assertEqual(rect_test1.id, rect_test2.id -1)

    def test_val2(self):
        """Check vlid input"""
        rect_tes1 = Rectangle(3, 4)
        rect_test2 = Rectangle(4, 9)
        rect_test3 = Rectangle(12, 3, 10)
        slef.assertEqual(rect_test.id, rect_test3.id -3)

    def test_val3(self):
        rect_test1 = Rectangle (3, 5)
        rect_test2 = Rectangle(4, 10)
        rect_test3 = Rectangle(9, 2, 4)
        rect_test4 = Rectangle(8, 4, 10 , 5)
        self.assertEqual(rect_test1.id, rect_test4.id - 3)

    def test_val4(self):
        rest_test1 = Rectangle(4, 2)
        rect_test2 = Rectangle(3, 9)
        rect_test3 = Rectangle(12, 4, 9)
        rect_test4 = Rectangle(9, 3, 4, 5)
        rect_test5 = Rectangle(10, 9, 15, 4, 12)
        self.assertEqual(Rectangle(10, 9, 15, 4, 11).id, 53)

    def test_neg_arg(self):
        rect_arg1 = Rectangle(12, 4, 9, -11)
        self.assertEqual(rect_arg1.id, -11)

    def test_poe_arg(self):
        rect__arg2 = Rectangle(12, 4, 9, 9)
        self.assertEqual(rect_arg2.id, 34)

    def test_str_ar(self):
        rect_str = Rectangle(8, 3, 7, "ALX")
        self.assertEqual(rect_str.id, "ALX")

    def test_err_type(self):
        Base.__nb_objects = 0
        with self.assetRaiseRegex(TypeError, "width must be an integer"):
            Rectangle("String", 3)
            Rectangle("Ture", 9)
        with self.assertRaiseRegex(TypeError, "height must be an integer"):
            Rectsngle(5, "School")
            Rectangle(7, "Savy")
    def test_val_err(self):
        """Testing out Value error riased"""
        with self,assertRaisesReges(ValueError, "width must be > 0"):
            Rectangle(0, 9)
            Rectangle(-4, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -5)
            Rectangle(9, 0)

    def  test_no_args(self):
        """Checks out error for no argument"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(9, None)
            Rectangle(None, 4)

    def test_errstr_arg(self):
        with self.assertRaises(TypeError):
            Rectangle (19, "Help")

    def test_no_args(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 9)

    def test_sero_arg(self):
        with self.assertRaises(ValueError):
            Rectangle (0, 0, 0, 0, 0)

    def test_non_int_arg(self):
        with self,assertRaises(TypeError):
            Rectangle(9, 3.9, 1.4, 1, 10)




