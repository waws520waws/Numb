# argparse  专门用来解析sys.argv
# 做自动化脚本的时候，用的特别多
import argparse
# 1.创建解析对象
parser = argparse.ArgumentParser()

"""
1.sender -s --sender
2.To_list   -t  --to_list  []
3.Cc_list   -c  --cc_list []
4.subject  -sj   --subject
5.auth_pwd  -ap  --auth_pwd
6.smtp_server  -smtp --smtp_server
"""
parser.add_argument("-s","--sender",dest="sender",required=True,help="发件人")
parser.add_argument("-t","--to_list",dest="to_list",nargs="+",required=True,help="收件人")
parser.add_argument("-c","--cc_list",dest="cc_list",default=[],nargs="+",required=False,help="抄送人")
parser.add_argument("-sj","--subject",dest="subject",required=True,help="主题")
parser.add_argument("-a","--auth_pwd",dest="auth_pwd",required=True,help="授权码")
parser.add_argument("-smtp","--smtp_server",dest="smtp_server",required=False,help="邮件发送服务器")

result = parser.parse_args()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # 邮件的主题内容
from email.mime.image import MIMEImage   #图片
from email.mime.application import MIMEApplication   #附件

import smtplib

sender = result.sender

to_list = result.to_list

cc_list = result.cc_list
subject = result.subject
auth_pwd = result.auth_pwd

dic = {
    "126":"smtp.126.com",
    "qq":"smtp.qq.com",
    "163":"smtp.163.com"
}
if not result.smtp_server:
    # 计算smtp_server
    k = sender.split("@")[1].split(".")[0]
    v = dic.get(k)
    if v:
        smtp_server = v
    else:
        raise Exception("对不起，您输入的邮箱，对应的服务器是不存在的，请联系管理员进行解决")
else:
    smtp_server = result.smtp_server

em = MIMEMultipart()     # em 其实是message.Message的一个子类对象
em["subject"] = subject
em["From"] = sender
em["To"] = ",".join(to_list)
em["Cc"] = ",".join(cc_list)

content = MIMEText("我们都是好孩子，天真无邪的孩子")
em.attach(content)

smtp = smtplib.SMTP()
smtp.connect(smtp_server)

smtp.login(sender,auth_pwd)
smtp.send_message(em)
smtp.close()


# 超纲内容
# 将python程序打包成一个可执行文件，直接使用命令就可以完成脚本的调用
# pip install pyinstaller  windows中可以生成exe文件
# pyinstaller -F 整个文件形成一个可执行文件
# -D 整个文件形成一个可执行文件夹
# 命令：pyinstaller -F 发送邮件-命令.py -n email
