import unittest

from task import *


class Chasy(unittest.TestCase):
    def test_result_1(self):
        self.assertEqual(run(5, 0, 2), [10, 0])

    def test_result_2(self):
        self.assertEqual(run(2, 50, 4), [10, 0])

    def test_result_3(self):
        self.assertEqual(run(10, 15, 2), [20, 30])


if __name__ == '__main__':
    unittest.main()
