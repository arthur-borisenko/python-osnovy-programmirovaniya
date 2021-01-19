import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_3(self):
        console_test("""1
        2
        3""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''3'''))

    def test_exam_2(self):
        console_test("""3000
        1213
        2222""", lambda: main(), lambda out_text: self.assertEqual(out_text, '''3000'''))


if __name__ == '__main__':
    unittest.main()
