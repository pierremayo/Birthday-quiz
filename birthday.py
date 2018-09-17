"""
birthday.py
Author: Pierre Mayo
Credit: 
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month

todaydate = datetime.today().day

month = month_name[todaymonth]

name = input("Hello, what is your name? ")
month_input = input("Hey " + name + ", what's the name of the month you were born in? ")
year = int(input("And what year were you born in, " + name +"? "))
day = int(input("And the day? "))

if month_input == "January":
    month1 = 1
elif month_input == "February":
    month1 = 2
elif month_input == "March":
    month1 = 3
elif month_input == "April":
    month1 = 4
elif month_input == "May":
    month1 = 5
elif month_input == "June":
    month1 = 6
elif month_input == "July":
    month1 = 7
elif month_input == "August":
    month1 = 8
elif month_input == "September":
    month1 = 9
elif month_input == "October":
    month1 = 10
elif month_input == "November":
    month1 = 11
elif month_input == "December":
    month1 = 12

if month1 == 12 or 1 or 2:
    timeofyear = "winter"
elif month1 == 3 or 4 or 5:
    timeofyear = "spring"
elif month1 == 6 or 7 or 8:
    timeofyear = "summer"
elif month1 == 9 or 10 or 11:
    timeofyear = "fall"

if year < 1980:
    year1 = "stone age"
elif 1980 <= year <= 1989:
    year1 = "eighties"
elif 1990 <= year <= 1999:
    year1 = "nineties"
else: year1 = "two thousands"

if month_input == "October" and day == 31:
    print("You were born on Halloween!")
elif month_input == month and day == todaydate:
    print("Happy birthday!")
else: print(name + ", you are a " + timeofyear + " baby of the " + year1 + "! ")