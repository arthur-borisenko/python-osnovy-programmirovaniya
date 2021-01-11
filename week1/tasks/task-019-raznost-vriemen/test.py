import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_3(self):
        console_test("""5
        6
        7
        8
        9
        10""", lambda: main(), lambda out_text: self.assertEqual(out_text, '10983'))

    def test_exam_2(self):
        console_test("""1
        1
        1
        2
        2
        2""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''3661'''))


if __name__ == '__main__':
    unittest.main()
