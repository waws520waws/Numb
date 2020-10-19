from selenium import webdriver
import pytest
import time
# 这里不适用for循环对列表中数据进行遍历测试，是因为我们的测试一旦终止，后面的数据就没有办法进入到测试中，所以需要调整策略
# 优化方案
# 数据驱动

search_list = ["小米10 青春版5G","小米10 Pro","小米","小米CC9","小米CC9e","小米CC9 美图定制版"]

class Test_xiaomi_UI(object):
    def setup_class(self):
        # 打开浏览器
        driver = webdriver.Chrome("chromedriver.exe")
        driver.implicitly_wait(10)
        self.driver = driver
        driver.get("https://www.mi.com/")  # 访问对应的商城网页

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("item",search_list)
    def test_hot_UI(self,item):
        self.driver.find_element_by_id("search").send_keys(item+"\n")
        time.sleep(2)
        # 获取菜单下的所有的信息
        item_titles = self.driver.find_elements_by_css_selector(".goods-list .title")
        titles = [item.text for item in item_titles]
        for title in titles:
            assert item in title

if __name__ == '__main__':
    pytest.main(["案例_小米UI_search.py","-s"])
