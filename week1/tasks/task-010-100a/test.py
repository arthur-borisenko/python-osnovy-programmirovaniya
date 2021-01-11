import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_1(self):
        console_test('''''',
                     lambda: main(),
                     lambda out_text: self.assertEqual(out_text, 'A' * 100))


if __name__ == '__main__':
    unittest.main()
