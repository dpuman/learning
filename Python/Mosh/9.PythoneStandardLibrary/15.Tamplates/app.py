from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from smtplib import SMTP, SMTPException, SMTPAuthenticationError
from pathlib import Path
from string import Template
import smtplib

temp = Template(Path("testing//template.html").read_text())

message = MIMEMultipart()
message["from"] = "DipanKAr"

message["to"] = "dipankar15-10756@diu.edu.bd"

message["subject"] = "This Is Learning"
body = temp.substitute({"name": "Dipu"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("Testing//one.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    try:
        smtp.ehlo()

        smtp.login("dpumail.in@gmail.com", "211813114.dipu")

        smtp.send_message(message)
        print("done..")

    except SMTPAuthenticationError:
        print("The username and/or password you entered is incorrect")
    except:
        print("An error occurred")
