import unittest

from  API_Project.tools.case import TestMathMethod

suit=unittest.TestSuite()  #存储用例

# suit.addTest(TestMathMethod('test_multi'))

# 方法二
#  TestLoader

loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(TestMathMethod))

runner=unittest.TextTestRunner()
runner.run(suit)