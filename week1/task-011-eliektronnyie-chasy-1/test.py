import unittest

from task import *


class Chasy(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(resultFunc(150), [2, 30])

    def test_result_2(self):
        self.assertEqual(resultFunc(150), [2, 30])

    def test_result_3(self):
        self.assertEqual(resultFunc(3498), [10, 18])


if __name__ == '__main__':
    unittest.main()
