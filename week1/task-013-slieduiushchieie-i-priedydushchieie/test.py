import unittest

from task import *
from util.TestUtil import console_test

class Test(unittest.TestCase):
    def test_print_sep(self):
        console_test("678",lambda:main(),lambda out_text:self.assertEqual(out_text,'''The next number for the number 678 is 679.
 The previous number for the number 678 is 677.'''))

if __name__ == '__main__':
    unittest.main()
