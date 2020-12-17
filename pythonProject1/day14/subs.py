import unittest
from day14.jisuanqi import Calc
class TestCalc1(unittest.TestCase):
    def testSubs(self):
        a = 3
        b = 2
        sum = 1
        c = Calc()
        s = c.subs(a,b)
        self.assertEqual(sum,s)


