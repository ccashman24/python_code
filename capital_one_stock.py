'''
CAPITAL ONE STOCK PRICE
LAST UPDATED: 2024-06-30
'''

import yfinance as yf
import xlsxwriter as excel
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
print()

# DEFINE THE STOCK SYMBOL - CAPITAL ONE (COF)
stock_symbol = 'COF'

def get_current_price(stock_symbol):
    cof_ticker = yf.Ticker(stock_symbol)
    print(get_current_price)

# get_current_price(stock_symbol)
# print(get_current_price)

cof_ticker = yf.Ticker(stock_symbol).info

current_date = datetime.now().strftime('%Y-%m-%d')

market_price = cof_ticker['currentPrice']
previous_close_price = cof_ticker['regularMarketPreviousClose']

print('Stock: Capital One (COF)')
print('Current Market Price: $', market_price)
print('Previous Close Price: $', previous_close_price)





# Creating Excel file to attach stock data

stock_workbook = excel.Workbook('stock_data.xlsx')

print()