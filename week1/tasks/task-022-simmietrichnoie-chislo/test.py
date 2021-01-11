import unittest

from task import *


class Test(unittest.TestCase):
    def test_exam_3(self):
        self.assertEqual(simetric_check("0909"),0)

    def test_exam_2(self):
        self.assertEqual(simetric_check("0880"),1)

    def test_fill_exam_1(self):
        self.assertEqual(fill("909"), "0909")


if __name__ == '__main__':
    unittest.main()
