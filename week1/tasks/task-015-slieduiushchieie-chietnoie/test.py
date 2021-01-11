import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_even(self):
        console_test("9346", lambda: main(), lambda out_text: self.assertEqual(out_text, '''9348'''))

    def test_not_even(self):
        console_test("9807", lambda: main(), lambda out_text: self.assertEqual(out_text, '''9808'''))


if __name__ == '__main__':
    unittest.main()
