from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()
message["from"] = "DipanKAr"
message["to"] = "dipankar15-10756@diu.edu.bd"
message["subject"] = "This Is Learning"
message.attach(MIMEText("BOdy"))
message.attach(MIMEImage(Path("Testing//one.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()

    smtp.login("dpumail.in@gmail.com", "211813114.dipu")

    smtp.send_message(message)
    print("done..")
