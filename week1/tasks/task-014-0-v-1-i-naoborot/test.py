import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_0_v_1(self):
        console_test("0", lambda: main(), lambda out_text: self.assertEqual(out_text, '''1'''))

    def atest_1_v_0(self):
        console_test("1", lambda: main(), lambda out_text: self.assertEqual(out_text, '''0'''))


if __name__ == '__main__':
    unittest.main()
