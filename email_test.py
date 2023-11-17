# Setting up Python test
# Last updated: 9/16/23
# SMTP = Simple Mail Transfer Protocol

import os
# import sys
import smtplib
from smtplib import SMTP
from dotenv import load_dotenv, find_dotenv
# dotenv_values
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# from email.mime.base import MIMEBase
# from email import encoders

print()
load_dotenv(find_dotenv())
path = 'C:/Users/ccash/python_code/env_setup.env'
load_dotenv(path)

# Define variables
appPassword = os.getenv("GMAIL_APP_KEY")

# print(appPassword)

emailSender = os.getenv("GMAIL_ADDR")
emailReceiver = os.getenv("GMAIL_ADDR")

testString = 'Stock: Capital One (COF)'

msg = MIMEMultipart()
msg['From'] = emailSender
msg['To'] = emailReceiver
msg['Subject'] = "Gmail Python Test"
body = "Testing sending an email via Gmail in Python" + \
        "\n testing print statement here - " + str(testString)
msg.attach(MIMEText(body, "plain"))

# baseInstance = MIMEBase('application', 'octet-stream')
# baseInstance.set_payload()
# encoders.encode_base64(baseInstance)

# Creates SMTP session
emailSession: SMTP = smtplib.SMTP('smtp.gmail.com', 587)

# Initiate Transfer Layer Security (TLS) for security
emailSession.starttls()

emailSession.login(emailSender, appPassword)

emailMessage = msg.as_string()

emailSession.sendmail(emailSender, emailReceiver, emailMessage)

print('Email Sent!')
print()

emailSession.quit()
