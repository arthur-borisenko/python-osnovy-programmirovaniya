import unittest

from task import start
from util.TestUtil import console_test


class Test(unittest.TestCase):

    def test_q_1(self):
        console_test("""17.9""", lambda: start(), lambda out_text: self.assertEqual(out_text, """0.9"""))

    def test_q_2(self):
        console_test("""10.34""", lambda: start(), lambda out_text: self.assertEqual(out_text, """0.34"""))

    def test_q_3(self):
        console_test("""0.001""", lambda: start(), lambda out_text: self.assertEqual(out_text, """0.001"""))


if __name__ == '__main__':
    unittest.main()