from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText  # 邮件的主题内容
from email.mime.image import MIMEImage   #图片
from email.mime.application import MIMEApplication   #附件

import smtplib

sender = "16601203140@163.com"

to_list = [
    "2870612722@qq.com"
]

cc_list = [
    "18592050134@163.com"
]
subject = "今天的天气不错"
auth_pwd = "OHPWYSVFZQCJZDSL"

em = MIMEMultipart()
em["subject"] = subject
em["From"] = sender
em["To"] = ",".join(to_list)
em["Cc"] = ",".join(cc_list)

# 上传图片到服务器
img = MIMEImage(open("2.jpg",mode="rb").read())
# 规划个路径，方便后面的查找 前面的地址cid代替就行了，后面我们需要起一个这个图片标识的名字
img.add_header("Content-ID","haha")
em.attach(img)

# 邮件的正文html信息
# content = MIMEText("<h1>我们都是好孩子</h1>",_subtype="html")
# 在这里我们需要先将我们需要的图片上传到我们的smtp服务器，这样接收的人可以从服务器拿到图片信息
# src='cid:jay' 这个地方就是服务器上的图片地址
content = MIMEText("<img src='cid:haha'>hahahhah",_subtype="html")

em.attach(content)

smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")

smtp.login(sender,auth_pwd)
smtp.send_message(em)

smtp.close()