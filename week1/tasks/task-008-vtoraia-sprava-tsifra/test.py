import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_1(self):
        console_test('''73''',
                     lambda: main(),
                     lambda out_text: self.assertEqual(out_text, '7'))

    def test_2(self):
        console_test('''86766656789''', lambda: main(), lambda out_text: self.assertEqual(out_text, "8"))


if __name__ == '__main__':
    unittest.main()
