import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_1(self):
        console_test("""700
        750""", lambda: main(), lambda out_text: self.assertEqual(out_text, '2'))

    def test_exam_2(self):
        console_test("""123
        369""", lambda: main(), lambda out_text: self.assertEqual(out_text, '3'))


if __name__ == '__main__':
    unittest.main()
