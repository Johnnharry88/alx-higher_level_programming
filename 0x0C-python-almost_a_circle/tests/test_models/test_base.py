#!/usr/bin/python3
""" Module containing uit tests."""
import unitest
from models.base import  Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """ Condition of Test"""

    def test_no_id(self):
        """Test for no id"""
        x = Base()
        self.assertEqual(1, x.id)

    def test_id(self):
        """testing fot id number"""
        x = Base()
        self.assertEqual(50, x.id)

    def test_0_id(self):
        """Testing for zero id"""
        x = Base(0)
        self.assertEqual(0, x.id)

    def test_neg_id(self):
        """Testing for negative id"""
        x = Base(-20)
        self.assertEqual(-20, x.id)

    def test_string_id(self):
        """Testing for string id"""
        x = Base("Betty")
        self.assertEqual("Betty", x.id)

    def test_list_id(self):
        """Testing uut the list"""
        x = Base([3, 5, 7])
        self.assertEqual([3, 5, 7], x.id]

    def test_dict_id(self):
        """Testing for dict"""
        x = Base({"id": 100})
        self.assertEqual({"id": 100}, x.id)

    def test_tuple_id(self):
        """Testing out for tuple"""
        x = Base((1, 5))
        self.assertEqual((1, 5), x.id)

    def test_json_strtyp(self):
        """TEsting the json string"""
        r = Rectangle(3, 5)
        json_dicts = r.to_dictionary()
        j_string = Base.to_json_str([json_dicts])
        self.assertEqual(type(j_string), str)

    def test_json_val(self):
        """Testing out for json value"""
        s = Square(2, 6, 6, 102)
        j_dicts = s.to_dictionary()
        j_string = Base.to_json_str([j_dicts])
        self.assertEqual(json.loads(j-string), [{"id": 102, "y": 6, "size": 2, "x": 6}]}

    def test_json_None(self):
        """Testing out json sting having none"""
        s = Square(2, 6, 6, 102)
        j_dict = s.to_dictionary()
        j_string = Base.to_json_str(None)
        self.assertEqual(j_string, "[]")

    def test_jsonEmpty(self):
        """Testing out for empty json"""
        s = Square(2, 6, 6, 102)
        j_dict = s.to_dictionary()
        j_string = Base.to_json_string([])
        self.assertEqual(j_string, "[]")

class Test_Square(unittest.TestCase):
    """Class for testing Base class methods"""

    @classmethod
    def setUpClass(cls):
        """class method for doc tests"""
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """Test out for docstring documentation"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Testing for mehtod doc_string documentation"""
        for f in self.setup:
            self.assertTrue(len(f[1].__doc__) >= 1)

    def test_class_docstring(self):
        """Testing class cdocstring docs"""
        self.assertTrue(len(Base.__doc__) >= 1)
