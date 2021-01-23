import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_1(self):
        console_test("""3""", lambda: run(), lambda out_text: self.assertEqual(out_text, '''1'''))

    def test_exam_2(self):
        console_test("""-4""", lambda: run(), lambda out_text: self.assertEqual(out_text, '''-1'''))
    def test_exam_3(self):
        console_test("""0""", lambda: run(), lambda out_text: self.assertEqual(out_text, '''0'''))
    def test_exam_4(self):
        console_test("""200""", lambda: run(), lambda out_text: self.assertEqual(out_text, '''1'''))
if __name__ == '__main__':
    unittest.main()