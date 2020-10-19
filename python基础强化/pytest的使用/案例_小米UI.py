from selenium import webdriver

from selenium.webdriver import ActionChains

# 打开浏览器
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.mi.com/")   # 访问对应的商城网页

xiaomi_menu = driver.find_element_by_css_selector("#J_navCategory+li")

# 模拟鼠标悬停
ac = ActionChains(driver)
ac.move_to_element(xiaomi_menu).perform() # 将鼠标定位到元素所在位置
import time
time.sleep(2)

# 获取菜单下的所有的信息
items = driver.find_elements_by_css_selector("#J_navMenu .title")
"""
['', '', '小米10', '小米10 青春版 5G', '小米MIX Alpha']
代码的运行速度快于页面中元素的展示速度，所以元素没有加载出来，程序就跳过去了，没有获取到
相对应的元素
让程序延迟一会，等待页面的元素加载完成
['小米10至尊纪念版', '小米10 Pro', '小米10', '小米10 青春版 5G', '小米MIX Alpha']
"""

titles = [item.text for item in items]

assert titles == ['小米10至尊纪念版', '小米10 Pro', '小米10', '小米10 青春版 5G', '小米MIX Alpha']
driver.quit()