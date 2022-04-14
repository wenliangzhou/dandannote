import unittest
# 0.TestCase 写用例
# 1.Testsuite 存储用例
# 2.TestLoader 找测试用例，存到1中
# 3.添加断言 assert
# 4。TextTestRunner  出测试报告
import requests

# 写一个测试类
class MathMehod:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def  add(self):
        return  self.a+self.b

    def multi(self):
        return  self.a*self.b

