import unittest

from task import startFile
from util.TestUtil import console_test


class Test(unittest.TestCase):

    def test_q_1(self):
        console_test("""3""", lambda: startFile(), lambda out_text: self.assertEqual(out_text, """1.36111"""))

    def test_q_2(self):
        console_test("""2""", lambda: startFile(), lambda out_text: self.assertEqual(out_text, """1.25"""))

    def test_q_3(self):
        console_test("""1""", lambda: startFile(), lambda out_text: self.assertEqual(out_text, """1.0"""))


if __name__ == '__main__':
    unittest.main()
