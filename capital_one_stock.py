import yfinance as yf
import xlsxwriter as excel
import pandas
from datetime import datetime

print()

#import matplotlib.pyplot as plt

# Define the stock symbol (Capital One)
stock_symbol = "COF"

#def get_current_price(stock_symbol):
#    cof_ticker = yf.Ticker(stock_symbol)


cof_ticker = yf.Ticker(stock_symbol).info

current_date = datetime.now().strftime('%Y-%m-%d')

market_price = cof_ticker['currentPrice']
previous_close_price = cof_ticker['regularMarketPreviousClose']

print('Stock: Capital One (COF)')
print('Current Market Price:', market_price)
print('Previous Close Price:', previous_close_price)





# Creating Excel file to attach stock data

stock_workbook = excel.Workbook('stock_data.xlsx')

print()