import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_1(self):
        console_test('''2''',
                     lambda: main(),
                     lambda out_text: self.assertEqual(out_text, '''4'''))
    def test_2(self):
        console_test('''5''',lambda :main(),lambda out_text:self.assertEqual(out_text,"32"))


if __name__ == '__main__':
    unittest.main()
