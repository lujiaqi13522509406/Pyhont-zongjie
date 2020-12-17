import unittest
from day15.jisuanqi import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [[3,1,3],
        [10,5,2],
        [20,2,10]]
@ddt
class TestCalDivi(unittest.TestCase):
    @data(*data1)
    @unpack
    def testDivi(self,q,w,e):
        a = q
        b = w
        c = e

        calc = Calc()
        sum = calc.divi(a,b)

        self.assertEqual(sum,c)

