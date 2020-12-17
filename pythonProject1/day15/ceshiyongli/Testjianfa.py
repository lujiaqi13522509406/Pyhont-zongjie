

import unittest
from day15.jisuanqi import Calc
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = [[3,2,1],
        [5,3,2],
        [7,4,3]]
@ddt
class TestCalSubs(unittest.TestCase):
    @data(*data1)
    @unpack
    def testSubs(self,q,w,e):
        a = q
        b = w
        c = e

        calc = Calc()
        sum = calc.subs(a,b)

        self.assertEqual(sum,c)