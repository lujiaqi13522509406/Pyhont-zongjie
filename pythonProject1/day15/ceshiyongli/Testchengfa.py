import unittest
from day15.jisuanqi import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [[1,2,2],
        [2,3,6],
        [3,4,12]]
@ddt
class TestCalMult(unittest.TestCase):
    @data(*data1)
    @unpack
    def testMult(self,q,w,e):
        a = q
        b = w
        c = e

        calc = Calc()
        sum = calc.mult(a,b)

        self.assertEqual(sum,c)


