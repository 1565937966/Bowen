import smtplib as s
from email.mime.text import MIMEText
from email.header import Header
import time

counter = 0
host = "smtp.qq.com"
port = 587
username = "1565937966@qq.com"
password = "yqlhghxazhozhheh"
subject = "Correct Your Password Immediately!"
from_email = username
to_email = "jzhai126@gmail.com"
email_connect = s.SMTP(host, port)
email_connect.ehlo()
email_connect.starttls()
email_connect.login(username, password)
message = MIMEText("Boom Shakalaka", "text", "utf-8")
message['Subject'] = Header(subject, 'utf-8')
for i in range(0, 100):
    email_connect.sendmail(from_email, to_email, message.as_string())
    counter += 1
    print("Already send {} email".format(counter))
    time.sleep(15)
email_connect.quit()
