from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "LucoMoro"
message["to"] = "email_receiver"
message["subject"] = "This is a test"
body = template.substitute({"name": "John"})
#body = template.substitute(name="John")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("path_image").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email_sender", "password")
    smtp.send_message(message)
    print("Sent...")
