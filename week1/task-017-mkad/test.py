import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_1(self):
        console_test("""109
        2""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''0'''))

    def test_exam_2(self):
        console_test("""60
        2""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''11'''))


if __name__ == '__main__':
    unittest.main()
