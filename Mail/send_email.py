#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/14 11:23
# @Author  : su
# @File    : send_email.py
"""
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):    # 格式化一个邮件地址
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = input('From:  ')
password = input('Password:  ')
to_addr = input('To:  ')
smtp_server = input('SMTP Server:  ')    # smtp.gmail.com

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')    # 1 发送纯文本邮件（plain表示纯文本）
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')      # 2 发送HTML邮件

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)    # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
