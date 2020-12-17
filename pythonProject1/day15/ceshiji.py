import unittest
from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()

loader = unittest.defaultTestLoader
cases = loader.discover("D:\\Users\\86923\\PycharmProjects\\pythonProject1\\day15\\ceshiyongli",pattern="Test*.py")
suite.addTest(cases)



f = open("计算器。html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="计算器的测试报告",
    description="这是一个计算器的测试报告",
    verbosity=1,
)

runner.run(suite)






