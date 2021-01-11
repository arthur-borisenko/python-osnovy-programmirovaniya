import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_exam_3(self):
        console_test("3602", lambda: main(), lambda out_text: self.assertEqual(out_text, '1:00:02'))

    def test_exam_2(self):
        console_test("45", lambda: main(), lambda out_text: self.assertEqual(out_text, '''0:00:45'''))


if __name__ == '__main__':
    unittest.main()
