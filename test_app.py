"""import"""
import unittest
from .app import add2  # Import add2 directly without using relative import

class TestAdd2(unittest.TestCase):
    '''
    Test the add2 function in app.py
    '''

    def test_add2_with_positive_number(self):
        ''' 
        Test add2 with positive number

        '''
        self.assertEqual(add2(3), 5, "Should be 5")

    def test_add2_with_negative_number(self):
        '''
        Test add2 with negative number

        '''
        self.assertEqual(add2(-3), -1, "Should be -1")

    def test_add2_with_zero(self):
        '''
        Test add2 with zero

        '''
        self.assertEqual(add2(0), 2, "Should be 2")


if __name__ == '__main__':
    unittest.main()
