import smtplib
import email
from email.header import Header
from email.mime.text import MIMEText


smtp_obj = smtplib.SMTP_SSL('smtp.qq.com',465)
smtp_obj.login('1240906543@qq.com','jvwjexvqtpjobadd')


msg = MIMEText('这是一封离别信', 'plain', 'utf-8')
msg['From'] = Header('1240906543@qq.com')
msg['To'] = Header('2316498520@qq.com','utf-8')
msg['Subject'] = Header('只是一封离别信','utf-8')


smtp_obj.sendmail('1240906543@qq.com','2316498520@qq.com',msg.as_string())
