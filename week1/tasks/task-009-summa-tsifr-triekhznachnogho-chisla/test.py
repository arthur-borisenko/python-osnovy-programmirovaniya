import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_1(self):
        console_test('''869''',
                     lambda: main(),
                     lambda out_text: self.assertEqual(out_text, '23'))

    def test_2(self):
        console_test('''549''', lambda: main(), lambda out_text: self.assertEqual(out_text, "18"))


if __name__ == '__main__':
    unittest.main()
