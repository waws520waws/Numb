import pytest
import os
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
    pytest.main(["测试文件-allure.py","-s","--alluredir=tmp/my_allure_results"])
    os.system("allure serve tmp/my_allure_results")