from selenium import webdriver
import pytest
import time
from selenium.webdriver import ActionChains

class Test_xiaomi_UI(object):
    def setup_class(self):
        # 打开浏览器
        driver = webdriver.Chrome("chromedriver.exe")
        self.driver = driver
        driver.get("https://www.mi.com/")  # 访问对应的商城网页

    def teardown_class(self):
        self.driver.quit()

    def test_hot_UI(self):
        xiaomi_menu = self.driver.find_element_by_css_selector("#J_navCategory+li")

        # 模拟鼠标悬停
        ac = ActionChains(self.driver)
        ac.move_to_element(xiaomi_menu).perform() # 将鼠标定位到元素所在位置
        time.sleep(2)

        # 获取菜单下的所有的信息
        items = self.driver.find_elements_by_css_selector("#J_navMenu .title")
        """
        ['', '', '小米10', '小米10 青春版 5G', '小米MIX Alpha']
        代码的运行速度快于页面中元素的展示速度，所以元素没有加载出来，程序就跳过去了，没有获取到
        相对应的元素
        让程序延迟一会，等待页面的元素加载完成
        ['小米10至尊纪念版', '小米10 Pro', '小米10', '小米10 青春版 5G', '小米MIX Alpha']
        """
        titles = [item.text for item in items]
        assert titles == ['小米10至尊纪念版', '小米10 Pro', '小米10', '小米10 青春版 5G', '小米MIX Alpha']

    def test_hongmi_UI(self):
        xiaomi_menu = self.driver.find_element_by_css_selector("#J_navCategory+li+li")

        # 模拟鼠标悬停
        ac = ActionChains(self.driver)
        ac.move_to_element(xiaomi_menu).perform()  # 将鼠标定位到元素所在位置

        time.sleep(2)

        # 获取菜单下的所有的信息
        items = self.driver.find_elements_by_css_selector("#J_navMenu .title")

        titles = [item.text for item in items]
        assert titles == ['Redmi K30 至尊纪念版', 'Redmi K30 Pro 系列', 'Redmi K30 系列', 'Redmi 10X', 'Redmi Note 8', 'Redmi 9']

if __name__ == '__main__':
    pytest.main(["案例_小米UI_pytest.py","-s","--alluredir=./tmp/my_allure"])
    import os
    os.system("allure serve tmp/my_allure")