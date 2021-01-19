import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_1(self):
        console_test("""0
        0""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''0'''))
    def test_exam_2(self):
        console_test("""1213
        2222""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''2'''))
    def test_exam_3(self):
        console_test("""1213
        4""",lambda :main(),lambda out_text:self.assertEqual(out_text,'''1'''))


if __name__ == '__main__':
    unittest.main()
