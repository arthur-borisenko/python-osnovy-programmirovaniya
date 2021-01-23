import unittest
from task import run
from util.TestUtil import console_test

ans1 = """0.433013"""
q1 = """1
1
1"""
ans2 = """30.0"""
q2 = """5
12
13"""


class Check(unittest.TestCase):
    def test_ans_1(self):
        asserting=lambda out_text: self.assertEqual(out_text,ans1)
        console_test(q1,lambda :run(),asserting)
    def test_ans_2(self):
        asserting=lambda out_text: self.assertEqual(out_text,ans2)
        console_test(q2,lambda :run(),asserting)
