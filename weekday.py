# Problem Task 04 (18/02/21)

# This program outputs whether or not today is a weekday

# Author: Caoimhin Vallely

# imports datetime module
import datetime

# creates variable for today - 'what_day_is_it'
# .today() - current date
# .weekday() - current day as an integer (0 to 6 - Mon to Sun)
what_day_is_it = datetime.datetime.today().weekday()

# if less than 4, i.e. Mon-Thur
if what_day_is_it < 4:
    print ("Still a bloody weekday!! :(")
elif what_day_is_it == 4: # if it's Friday!
    print ("Still a weekday but we're very nearly there!!")
else:  # otherwise it's 5/6 which is Sat/Sun
    print ("Praise the lord it's the weekend!!! :)")