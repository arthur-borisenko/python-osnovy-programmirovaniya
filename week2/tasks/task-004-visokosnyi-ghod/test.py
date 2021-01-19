import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_1(self):
        console_test("""1""", lambda: start(), lambda out_text: self.assertEqual(out_text, '''NO'''))

    def test_exam_2(self):
        console_test("""4""", lambda: start(), lambda out_text: self.assertEqual(out_text, '''YES'''))
    def test_exam_3(self):
        console_test("""400""", lambda: start(), lambda out_text: self.assertEqual(out_text, '''YES'''))
    def test_exam_4(self):
        console_test("""200""", lambda: start(), lambda out_text: self.assertEqual(out_text, '''NO'''))
if __name__ == '__main__':
    unittest.main()