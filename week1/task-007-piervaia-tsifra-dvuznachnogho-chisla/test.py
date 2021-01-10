import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_1(self):
        console_test('''47''',
                     lambda: main(),
                     lambda out_text: self.assertEqual(out_text, '''4'''))
    def test_2(self):
        console_test('''32''',lambda :main(),lambda out_text:self.assertEqual(out_text,"3"))


if __name__ == '__main__':
    unittest.main()
