## Exercise 1: Print Strings :ballot_box_with_check:
Write a Python program to print the following string in a specific format.

print("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are.")

## Exercise 2: Print the Version of Python :ballot_box_with_check:
Write a Python program to get the Python version you are using.

import sys
from tkinter.ttk import Notebook
print(sys.version)

## Exercise 3: Print date and Time :ballot_box_with_check:
Write a Python program to display the current date and time.

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

## Exercise 4: Strings Concatination :ballot_box_with_check:
Write three strings in different variables and print the output as one string.

a = "Notebook"
b = "Assignment"
c = "Room"

print(a)
print(b)
print(c)
print(a+b+c)

## Exercise 5: Compute area of Circle :ballot_box_with_check:
Write a Python program which accepts the radius of a circle from the user and compute the area.

# import math module
from math import pi
 
# take input from user
r = float(input ("Input the radius of the circle : "))
 
# compute the area from radius of a circle given by user
calculateArea = str(pi * r**2);
 
#print result
print ("The area of the circle with radius " + str(r) + " is: " + calculateArea)