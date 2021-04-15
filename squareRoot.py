# Problem Task 05 (27/02/21)

# Author: Caoimhin Vallely

# This program takes a users inputted number and returns an approximation of its square root using the Newton method. 
# Use of built-in functions was forbidden!

# Newton's method involves a guess which I don't think was in the remit of this task
# so I'm going with a random number and sufficient iterations of the formula.

import random # imports random module

# defining the function <<sqrt>>
def sqrt(A):
    A = random.uniform(1, user_number) # generates a random positve number between 1 and the inputted number
    while True: # starts off a while loop
        B = 0.5 * ((user_number / A) + A) # Newton's method with result stored in B
        if (A - B) < 0.001: # this tests the difference between each iteration and if it's less than 0.001 we 
            return B       # exit the function and the final B is returned
        A = B              # otherwise we go again until the 'if' statement is realised

# main program
user_number = float(input("Please enter a postive number: ")) # asks user to enter a number and converts it to a float
if user_number < 0: # bit of error handling
    print ("I said a POSITIVE number!!")
else:
    result = sqrt(user_number) # calls the function and runs the users inputted number through it
    rounded_result = round(result, 1) # rounds the result to 1 decimal place as implied in the brief
    print("The square root of ", user_number, "is approximately ", rounded_result) # prints the answer