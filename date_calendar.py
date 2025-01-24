"""
Author: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 18/01/25
python code that calculates the absolute difference between the current date and a future or past
IDE: pydriod
Script title: Difference in dates
"""
from datetime import datetime

# Write a one-liner that substracts the difference between two dates.
def diff_in_days(start, end): return abs(end-start).days
  
# Collect the data of our targeted dates as integers
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Using datetime we collect the current date
start = datetime.now()
# Convert our collected integer variables to date variables
end = datetime(year, month, day)

# Initialize our oneline function
if __name__ == "__main__":
  print(diff_in_days(start, end))
