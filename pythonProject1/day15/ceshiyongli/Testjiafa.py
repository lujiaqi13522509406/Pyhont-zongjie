import unittest
from day15.jisuanqi import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [[1,2,3],
        [2,3,5],
        [3,4,7]]
@ddt
class TestCalAdd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,q,w,e):
        a = q
        b = w
        c = e

        calc = Calc()
        sum = calc.add(a,b)

        self.assertEqual(sum,c)

