"""
Author: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 17/01/25
python script to display dates of a month in cli
"""

import calendar as c

def display_calendar():
  year = int(input("Enter the year: "))
  month = int(input("Enter the month number here: "))
  cal = c.TextCalendar(c.Monday)
  month_cal = cal.formatmonth(year, month)
  print(month_cal)
if __name__ == "__main__":
  dislay_calendar()
