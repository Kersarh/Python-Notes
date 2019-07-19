# -*- coding: utf-8 -*-

import smtplib
import email
import mimetypes
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.header import Header
from base64 import encodebytes

# Параметры SMTP-сервера
mail_from   = "from@gmail.com" # отправитель
mail_to     = "to@gmail.com"   # получатель
mail_text   = "Тестовое письмо!nПослано из python" # текст письма
mail_subj   = "Тестовое письмо" # заголовок письма
mail_coding = "windows-1251"
attach_file = "" #["D:\\test.txt", "D:\\test2.txt"] # прикрепляемый файл

smtp_server = "smtp.gmail.com"
smtp_port   = 587
smtp_user   = "from@gmail.com" # пользователь smtp
smtp_pwd    = "pass"           # пароль smtp
 
# формирование сообщения
multi_msg = MIMEMultipart()
multi_msg['From'] = Header(mail_from, mail_coding)
multi_msg['To'] = Header(mail_to, mail_coding)
multi_msg['Subject'] =  Header(mail_subj, mail_coding)
 
msg = MIMEText(mail_text.encode('cp1251'), 'plain', mail_coding)
msg.set_charset(mail_coding)
multi_msg.attach(msg)
 
# атач-файл
for add_file in attach_file:
	if(os.path.exists(add_file) and os.path.isfile(add_file)):
	    file = open(add_file, 'rb')
	    attachment = MIMEBase('application', "octet-stream")
	    attachment.set_payload(file.read())
	    email.encoders.encode_base64(attachment)
	    file.close()
	    only_name_attach = Header(os.path.basename(add_file),mail_coding);
	    attachment.add_header('Content-Disposition','attachment; filename="%s"' % only_name_attach)
	    multi_msg.attach(attachment)
	else:
	    if(add_file.lstrip() != ""):
	        print("Файл для атача не найден - " + add_file)

# Отправка
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(smtp_user, smtp_pwd)
smtp.sendmail(mail_from, mail_to, multi_msg.as_string())
smtp.quit()

os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
