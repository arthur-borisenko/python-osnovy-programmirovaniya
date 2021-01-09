import unittest

from task import *
from util.TestUtil import console_test


class Test(unittest.TestCase):
    def test_hello(self):
        console_test("Harry",
                     lambda: hello(),
                     lambda out_text: self.assertEqual(out_text, "Hello, Harry!\n"))


if __name__ == '__main__':
    unittest.main()
