
# email这个包是用来构建整个邮件，邮件的各个组成部分(发送人、接收人、抄送人、主题)+邮件的正文
# smtplib这个包是用来发送邮件的

from email.mime.multipart import MIMEMultipart
# 一封邮件：一份邮件是由很多的部分组成的，谁发的，发给谁，附件，图片，抄送给谁
from email.mime.text import MIMEText  # 邮件的主题内容
from email.mime.image import MIMEImage   #图片
from email.mime.application import MIMEApplication   #附件

# 发送邮件使用smtplib
import smtplib

# 准备发送邮件的参数
# 发邮件的人
sender = "16601203140@163.com"

# 收件人
to_list = [
    "2870612722@qq.com"
]

# 抄送的人
cc_list = [
    "18592050134@163.com"
]

# 邮件的主题
subject = "今天的天气不错"

# 授权码:使用账号密码进行登录的好，我们程序会泄露我们的密码，授权码相当于是连接的加密，连接smtp服务器
auth_pwd = "OHPWYSVFZQCJZDSL"
"""
你要连人家的smtp服务器就需要连个东西：(1)用户名 xxxxxx@163.com (2)授权码：xxxxx
"""


# 写邮件
# 创建邮件
em = MIMEMultipart()     # em 其实是message.Message的一个子类对象
em["subject"] = subject
em["From"] = sender
em["To"] = ",".join(to_list)
em["Cc"] = ",".join(cc_list)

# 邮件的正文信息
content = MIMEText("我们都是好孩子，天真无邪的孩子")

# 正文和邮件各个部分绑定
em.attach(content)


# 发送邮件
# 1.首先先要连接上人家的服务器
smtp = smtplib.SMTP()  # 创建连接对象
smtp.connect("smtp.163.com")  # 连接服务器

# 2.登录
smtp.login(sender,auth_pwd)

# 3.发送邮件
# 通过看参数我们能了解的就是这个地方需要的是message.Message的对象，实际上就是上面形式构造好的em对象
# 将邮件的各个部分进行封装，形成的一个整体
smtp.send_message(em)    # 其中from_addr和to_addr是不用写的，在我们的em构造对象中已经存在
"""
sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[])
实际上我们能够看出的就是这个地方是上面构造的各个部分，所有信息都是分开的
"""
#smtp.sendmail()

# 4.关闭连接
smtp.close()












