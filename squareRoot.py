# Problem Task 05 - Week06

# Author: Caoimhin Vallely

# This program takes a users inputted number and returns an approximation of its square root using the Newton method. 
# Use of built-in functions was forbidden!

# Newton's method involves a guess which I don't think was in the remit of this task
# so I'm going with a random number and lots of iterations of the formula.

import random # imports random module

# defining the function <<sqrt>>
def sqrt(A):
    A = random.uniform(1, user_number) # generates a random positve number between 1 and the inputted number
    for i in range(100): # sets it up to run the formula 100 times
        A = 0.5 * ((user_number / A) + A) # interpretted version of newton's method
    return A

# main program
user_number = float(input("Please enter a postive number: ")) # asks user to enter a number and converts it to a float
if user_number < 0: # bit of error handling
    print ("I said a POSITIVE number!!")
else:
    result = sqrt(user_number) # calls the function and runs the users inputted number through it
    rounded_result = round(result, 1) # rounds the result to 1 decimal place as suggested in brief
    print("The square root of ", user_number, "is approximately ", rounded_result) # prints the answer