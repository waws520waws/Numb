# argparse  专门用来解析sys.argv
# 做自动化脚本的时候，用的特别多
import argparse
# 1.创建解析对象
parser = argparse.ArgumentParser()

# 2.给定规则
# 2.1位置参数
# parser.add_argument("a")
# parser.add_argument("b")
# 2.2指令参数
parser.add_argument("-a",dest="jay")   # dest是设置变量名，接收-a的参数  -a 13 ---> jay = 13
# 2.2.1指令列表参数
# parser.add_argument("-b",dest="jj",nargs=5)  # 固定数量的列表
parser.add_argument("-b",dest="jj",nargs="+")  # +至少数量一个的列表，+是re替代符  * . ?都可以用

#  -b 参数可以给也可以不给给了用给定的数据，不给(就是直接不写-a)用默认值
# parser.add_argument("-b",dest="jj",default="哈哈")
# parser.add_argument("-b",dest="jj",type=int)  使用type规定类型

# 使用required=True规定这个参数是不是必须的，若是，不传(即使有默认值,也会报错)会报错
# parser.add_argument("-b",dest="jj",required=True)


# 多个参数连用
parser.add_argument("-a",dest="a",default=False,action="store_true")  # 实际上 store_true -a 出现就是True，不出现就是default
parser.add_argument("-b",dest="b",default=False,action="store_true")
parser.add_argument("-c",dest="c",default=False,action="store_true")

# "--xxxx" 进行详细说明
parser.add_argument("-a","--all",dest="c",default=False,action="store_true")


# 3.解析sys.args
result = parser.parse_args()  # 固定写法

# 从解析的结果中拿到数据
# print(result.a)
# print(result.b)
print(result.jay)
print(result.jj)
"""
命令：python argparse_test.py -a 13 -b 15 23 3 24 123
结果：
13
['15', '23', '3', '24', '123']
"""