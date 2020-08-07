#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/25 16:01
# @Author  : LOUIE

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.read_config import rc
from common.config_log import log
from smtplib import SMTP
import time
from smtplib import SMTP_SSL
from email.header import Header


class ConfigEmail:

    def __init__(self):
        self.email_host = rc.get_email("emai_host")
        self.email_port = rc.get_email("emai_port")
        self.username = rc.get_email("username")
        self.password = rc.get_email("password")
        self.value = rc.get_email("reciever")
        self.reciever = ["ceshi@tanzhou.cn"]
        self.subject = rc.get_email("subject")
        self.content = self.read_report()  # 获取测试报告
        self.msg = MIMEMultipart()
        self.smtp = SMTP()

    def read_report(self):
        with open(rc.REPORT_PATH, 'rb') as f:
            data = f.read()
        return data

    def email_content(self):

        # send_content = self.read_report()  # 获取测试报告
        # html = MIMEText(_text=send_content, _subtype='html', _charset='utf-8')  # 第一个参数为邮件内容
        content = MIMEText(self.content, _subtype='html', _charset="utf-8")
        self.msg.attach(content)

    def email_header(self):

        self.msg["To"] = ";".join(self.reciever)    # 接受者
        print(self.msg["To"])
        self.msg["From"] = Header(self.username, 'utf-8')          # 发送者
        self.msg["Subject"] = Header(self.subject, 'utf-8')          # 邮件主题

    # def check_file(self):
    #     """
    #     检查报告文件，并排序,提取最新生成的报告文件
    #     """
    #     REPORT_PATH = rc.REPORT_PATH
    #     file_lists = os.listdir(REPORT_PATH)        # 获取报告文件列表
    #     if len(file_lists) != 0:        # 判断文件列表是否为空
    #         LOG.error("##### Report Not Found //////")
    #         return FileNotFoundError
    #     # 对文件列表进行排序，根据mtime修改文件时间排序
    #     file_lists.sort(key=lambda x: os.path.getmtime(REPORT_PATH + "\\" + x))
    #     # 拿到排序后的最新文件
    #     att_file = os.path.join(REPORT_PATH, file_lists[-1])
    #     return att_file

    def email_attachment(self):

        # file = self.check_file()
        # att_file = MIMEText(file, 'base64', "utf-8")
        # date = time.strftime("%Y-%m-%d")
        # att_name = date + " # TestReport.html"      # 附件文件名称
        # att_file["Content-Disposition"] = 'attachment; filename={}'.format(att_name)
        # self.msg.attach(att_file)
        # 邮件正文内容 html 形式邮件

        # self.send_content = self.read_report()  # 获取测试报告
        # 构造附件
        att = MIMEText(_text=self.content, _subtype='base64', _charset='utf-8')
        att["Content-Type"] = 'application/octet-stream'
        date = time.strftime("%Y_%m_%d", time.localtime(time.time()))
        file_name = 'apiFlowAutoTest_' + date + ".html"
        att["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)  # # filename 为邮件附件中显示什么名字
        self.msg.attach(att)

    def send_email(self):

        self.email_header()
        self.email_content()
        self.email_attachment()

        try:
            # self.smtp.connect(self.email_host)
            self.smtp = SMTP_SSL(self.email_host)
            self.smtp.ehlo_or_helo_if_needed()
            self.smtp.login(self.username, self.password)
            # login的user参数与sendmail的from_addr参数需一致，否则报错501：mail from address must be same as authorization user
            self.smtp.sendmail(self.username, self.msg["To"].split(";"), self.msg.as_string())
            log.info("##### 邮件发送成功 ！！！！！")
        except TimeoutError:
            log.error("////// 发送邮件超时，请检查网络连接")
        except Exception as e:
            log.error("////// 发送邮件失败，错误：%s" %e)
        finally:
            # self.smtp.close()
            self.smtp.quit()


