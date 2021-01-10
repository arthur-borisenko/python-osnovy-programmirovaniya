import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_1(self):
        console_test('''2623747137614525''',
                     lambda: main(),
                     lambda out_text: self.assertEqual(out_text, '''5'''))
    def test_2(self):
        console_test('''73182318127127211289212''',lambda :main(),lambda out_text:self.assertEqual(out_text,"2"))


if __name__ == '__main__':
    unittest.main()
