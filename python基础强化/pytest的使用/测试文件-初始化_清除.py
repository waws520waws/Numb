import pytest
# 测试用例的定义--函数篇(套件就是.py文件本身)
# 用例规范(必须遵守):函数名称以test开头
# def setup_module():
#     print("执行用例初始化操作")
#     print("打开浏览器")
#
# def test_case001():
#     print("执行第一条测试用例")
#
# def test_case002():
#     print("执行第二条测试用例")
#
# def teardown_module():
#     print("执行用例清除操作")
#     print("关闭浏览器")


# ------------------------------------------
def setup_module():
    print("@@@@@执行用例初始化操作")
    print("@@@@@打开浏览器")


def teardown_module():
    print("@@@@@执行用例清除操作")
    print("@@@@@关闭浏览器")

class TestLogin(object):
    # 套件：就是将所有用例集合起来的统称就是套件
    def setup_class(self):
        print("执行用例初始化操作")
        print("打开浏览器")

    def test_case001(self):
        print("执行类方法测试用例11111######")

    def test_case002(self):
        print("执行类方法测试用例22222######")

    def teardown_class(self):
        print("执行用例初始化操作")
        print("打开浏览器")

if __name__ == '__main__':
    pytest.main(["测试文件-初始化_清除.py","-s"])