import unittest
from API_Project.tools.Method import MathMehod


class TestMathMethod(unittest.TestCase):
    #     编写测试用例
    #     一个用例就是一个函数,不能进行传参，只能有self关键字
    #     所有的用例都需要以test开头
    def test_add(self):
        res=MathMehod(1,2).add()
        print('相加结果:',res)
        self.assertEqual(2,res,msg='数据不对')

    def test_multi(self):
        res=MathMehod(1,2).multi()
        print('相加结果:',res)


if __name__ == '__main__':
    unittest.main()
# 执行顺序根据ASCII编写