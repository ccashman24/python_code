# Calculating future dates
from datetime import datetime, timedelta

print()

date_today = datetime.now().date()
print("Today's Date: ", date_today)
print()
 
# date_today_no_time = datetime.strptime(date_today, '%Y-%m-%d').date()
# print(date_today_no_time)
# print()

account_close_date = datetime(2023, 10, 18).date()
# account_close_date = account_close_date.days
print("Account close date: ", account_close_date)
print()
 
date_delta = timedelta(days=105)
# date_delta = date_delta.days
print(date_delta)
print()

date_calc = account_close_date + date_delta
# date_calc = date_calc.date()
print(date_calc)
print()