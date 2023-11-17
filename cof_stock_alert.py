# Capital One Stock Price Email Alert
# Last updated: 10/26/23
# SMTP = Simple Mail Transfer Protocol

import os
import re
import smtplib
import yfinance as yf
from smtplib import SMTP
from dotenv import load_dotenv, find_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print()

# Load in environment setup with Gmail information
load_dotenv(find_dotenv())
path = 'C:/Users/ccash/python_code/env_setup.env'
load_dotenv(path)

# Define variables
appPassword = os.getenv("GMAIL_APP_KEY")
emailSender = os.getenv("GMAIL_ADDR")
emailReceiver = os.getenv("GMAIL_ADDR")

# Define the stock symbol (Capital One)
stock_symbol = "COF"

# Initiate ticker instance
cof_ticker = yf.Ticker(stock_symbol).info

# Pull in current market price of stock
market_price = cof_ticker['currentPrice']
market_price = "${:.2f}".format(market_price)

# Pull in previous close price of stock
previous_close_price = cof_ticker['regularMarketPreviousClose']
previous_close_price = "${:.2f}".format(previous_close_price)

# Define print variables for email body
stock_symbol_print = 'Stock: Capital One (COF)'

current_market_price_print = 'Current Market Price: ' + str(market_price)
current_market_price_print = str(current_market_price_print)
current_market_price_print = re.sub(r'[()]', '', current_market_price_print)
current_market_price_print = current_market_price_print.replace("'", "")

previous_close_price_print = 'Previous Close Price: ' + str(previous_close_price)
previous_close_price_print = str(previous_close_price_print)
previous_close_price_print = re.sub(r'[()]', '', previous_close_price_print)
previous_close_price_print = previous_close_price_print.replace("'", "")

# Creating the details of the email
msg = MIMEMultipart()
msg['From'] = emailSender
msg['To'] = emailReceiver
msg['Subject'] = "Capital One Stock Info"
body = "Capital One Stock Information" + \
       "\n" + str(stock_symbol_print) + \
       "\n" + str(current_market_price_print) + \
       "\n" + str(previous_close_price_print)
msg.attach(MIMEText(body, "plain"))

# Creates SMTP session
emailSession: SMTP = smtplib.SMTP('smtp.gmail.com', 587)

# Initiate Transfer Layer Security (TLS) for security
emailSession.starttls()

emailSession.login(emailSender, appPassword)

emailMessage = msg.as_string()

emailSession.sendmail(emailSender, emailReceiver, emailMessage)

# print('Email Sent!')
print()

emailSession.quit()
