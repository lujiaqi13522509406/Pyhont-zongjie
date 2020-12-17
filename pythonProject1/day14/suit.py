import unittest
from day14.kuangjia import TestCal
from day14.subs import TestCalc1
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()

suite.addTest(TestCal("testAdd"))
suite.addTest(TestCal("testAdd1"))
suite.addTest(TestCalc1("testSubs"))

f = open("计算器.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "计算器的测试报告",
    description = "这是一个计算器的测试",
    verbosity = 1,
)


htmlrunner.run(suite)











