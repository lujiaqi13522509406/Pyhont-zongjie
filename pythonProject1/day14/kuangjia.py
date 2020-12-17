import unittest
from day14.jisuanqi import Calc
class TestCal(unittest.TestCase):

    def testAdd(self):
        a = 1
        b = 2
        sum = 3
        c = Calc()
        s = c.add(a,b)


        self.assertEqual(sum,s)

    def testAdd1(self):
        a = -1
        b = -2
        sum = -3
        c = Calc()
        s = c.add(a, b)

        self.assertEqual(sum,s)





