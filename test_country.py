import unittest
from rest_test.api import Country
import json


class test_constructor_class(unittest.TestCase):

    test_values_1 = {
        'region':'South America',
        'name':'Colombia',
        'capital':'Bogotá',
        'languages':'Español',
        'time':1234
    }

    test_values_2 = {
        'region':'South America',
        'name':'Colombia',
        'capital':'Bogotá',
        'languages':'Español',
    }

    test_values_3 = {
        'region':'',
        'name':'',
        'capital':'',
        'languages':'',
    }

    test_values_4 = {}

    def test_constructor_inital_values(self):
        obj = Country(self.test_values_1)
        self.assertEqual(obj.region,'South America')
        self.assertEqual(obj.name,'Colombia')
        self.assertEqual(obj.capital,'Bogotá')
        self.assertEqual(obj.languages,'Español')
        self.assertFalse(obj.time,1234)

    def test_constructor_no_time(self):
        obj = Country(self.test_values_2)
        self.assertEqual(obj.region,'South America')
        self.assertEqual(obj.name,'Colombia')
        self.assertEqual(obj.capital,'Bogotá')
        self.assertEqual(obj.languages,'Español')
        self.assertEqual(obj.time,0)

    def test_constructor_empty_values(self):
        obj = Country(self.test_values_3)
        self.assertEqual(obj.region,'')
        self.assertEqual(obj.name,'')
        self.assertEqual(obj.capital,'')
        self.assertEqual(obj.languages,'')
        self.assertEqual(obj.time,0)

    def test_constructor_no_values(self):
        obj = Country(self.test_values_4)
        self.assertEqual(obj.region,None)
        self.assertEqual(obj.name,None)
        self.assertEqual(obj.capital,None)
        self.assertEqual(obj.languages,None)
        self.assertEqual(obj.time,0)

    def test_constructor_types(self):
        obj = Country(self.test_values_1)
        self.assertTrue(type(self.test_values_1) is dict)
        self.assertTrue(type(obj.region) is str)
        self.assertTrue(type(obj.name) is str)
        self.assertTrue(type(obj.capital) is str)
        self.assertTrue(type(obj.languages) is str)
        self.assertTrue(type(obj.time) is int)

if __name__ == '__main__':
    unittest.main()
