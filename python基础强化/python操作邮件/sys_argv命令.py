print("hahahh")
import argparse

import sys   # 系统--> python的解释器解释器系统
# import os  # 操作系统 --> 对于文件，文件夹系统
print(sys.argv)   # 获取到命令行参数

"""
命令行：python sys_argv命令.py -u root -p 123 -m "haha"
打印的实际的参数：
['sys_argv命令.py', '-u', 'root', '-p', '123', '-m', 'haha']  可以提取出来使用
"""

# sys.path  模块的搜索路径
# import hhhh   sys.path 按照这个列表中的路径进行查找，一个一个排查
print(sys.path)
"""
['C:\\Users\\waws\\Desktop\\leetcode', 'C:\\Users\\waws\\Desktop\\leetcode', 
'C:\\Users\\waws\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip', 
'C:\\Users\\waws\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 
'C:\\Users\\waws\\AppData\\Local\\Programs\\Python\\Python36\\lib', 
'C:\\Users\\waws\\AppData\\Local\\Programs\\Python\\Python36', 
'C:\\Users\\waws\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages', 
'C:\\Program Files\\JetBrains\\PyCharm 2017.3.3\\helpers\\pycharm_matplotlib_backend']
"""

print(sys.getdefaultencoding())
# utf-8



