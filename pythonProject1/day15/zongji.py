import unittest
from day14.danyuanceshi import TestBank
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

# suite.addTest(TestBank("testtakeMoney"))
# suite.addTest(TestBank("testtakeMoney1"))
# suite.addTest(TestBank("testtakeMoney2"))
# suite.addTest(TestBank("testtakeMoney3"))


#获取加载器

loader = unittest.defaultTestLoader

cases = loader.discover("D:\\Users\\86923\\PycharmProjects\\pythonProject1\\day15\\testcase",pattern="Test*.py")

suite.addTest(cases)




f = open("银行取钱.html","w+",encoding="utf-8")

htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title="银行取钱的测试报告",
    description="这是一个银行取钱的测试",
    verbosity=1,

)

htmlrunner.run(suite)

