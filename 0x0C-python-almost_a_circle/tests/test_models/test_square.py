#!/usr/bin/python3
"""defines unnitest for square.py"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestSquare_instiationa(unittest.TestCase):
    """Test for Instiantiation of Square class"""
    
    def test_base(self):
        self.assertIsInstance(Square(5), Base)

    def Test_rect(self):
        self.assertIsInstance9Square(7), Rectangle)

    def test_no_args(self):
        with self.assertRaises(TypeError)
        Square()

    def test_3_values(self):
        squ1 = Square(3, 8)
        squ2 = Square(3, 9)
        squ3 = Square(8, 9, 4)
        self.assertEqual(squ1.id, squ3.id -2)

    def test_id_no(self):
        self.assertEqual(6, Square91, 3, 4, 6).id)
    
    def test_str_id(self):
        self.assertEqual("ALX", Square(3, 5, 5,"ALX").id)

    def test_get_size)self):
        self.assertEqual(2, Square(2, 3, 4, 9).size)

