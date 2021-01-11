import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_3(self):
        console_test("""20
        3
        2""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''18'''))
    def test_exam_2(self):
        console_test("""10
        3
        2""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''8'''))


if __name__ == '__main__':
    unittest.main()
