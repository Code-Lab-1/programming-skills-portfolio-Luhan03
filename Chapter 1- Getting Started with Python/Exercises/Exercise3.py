## Exercise 3: Print date and Time

from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("Year:", year)

month = now.strftime("%B")
print("Month:", month)

day = now.strftime("%d")
print("Day:", day)

time = now.strftime("%I:%M:%S")
print("Time:", time)

date_time = now.strftime("%B %d,%Y, %I:%M:%S")
print("Date and Time:",date_time)
