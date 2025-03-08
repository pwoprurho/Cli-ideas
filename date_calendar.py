"""
Author: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 18/01/25
python code that calculates the absolute difference between the current date and a future or past
IDE: pydriod
Script title: Difference in dates
"""
import calendar as c

def display_calendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month here: "))
    try:
        if month <= 12:
            cal = c.TextCalendar(c.SUNDAY)
            month_cal = cal.formatmonth (year, month)
        print(month_cal)
    except TypeError:
        print("Invalid input please try a numeric input")
    
if __name__ == "__main__":
    display_calendar()