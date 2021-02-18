# Write a program that outputs whether or not today is a weekday.
# Author: Caoimhin Vallely

# imports datetime module
import datetime

# creates variable for today
# .today - current date
# .weekday - current day as an integer (0 to 6 - Mon to Sun)
whatDayIsIt = datetime.datetime.today().weekday()

# if less than 5, i.e. Mon-Fri
if whatDayIsIt < 5:
    print ("Still a weekday!! :(")
else:  # otherwise it's 5/6 which is Sat/Sun
    print ("Praise the lord it's the weekend!!! :)")