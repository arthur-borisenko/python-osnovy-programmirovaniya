example1 = """44
55
55
44"""
example2 = """4
4
5
5"""
example3 = """55
44
55
44"""
example4 = """55
46
55
44"""
answer1 = """NO"""
answer2 = """YES"""
answer3 = """YES"""
answer4 = """NO"""


import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_1(self):
        console_test(example1, lambda: run(), lambda out_text: self.assertEqual(out_text, answer1))

    def test_exam_2(self):
        console_test(example2, lambda: run(), lambda out_text: self.assertEqual(out_text, answer2))
    def test_exam_3(self):
        console_test(example3, lambda: run(), lambda out_text: self.assertEqual(out_text, answer3))
    def test_exam_4(self):
        console_test(example4, lambda: run(), lambda out_text: self.assertEqual(out_text, answer4))


if __name__ == '__main__':
    unittest.main()

