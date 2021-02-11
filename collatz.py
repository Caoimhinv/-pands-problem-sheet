# This program asks the user to input any positve integer
# At each step it calculates the next value 
# by taking the current value and, if it is even,
# divides it by two, but if it is odd, 
# multiplies it by three and adds one.

# The program ends if the current value is one.

# Author: Caoimhin Vallely

# creating a function (beyond me as of 11/2/21!!)
def problemWeek4(number):
    if number % 2 == 0: # checking if number is even 
        number = number // 2 # dividing by 2
    else:
        number = number * 3 + 1 # multiplying by 3 and adding 1
    print(number)
    return(number)

userNumber = int(input("Please enter a positive integer: ")) # asks user to enter number

while (userNumber != 1): # stops programming when number hits 1
    userNumber = problemWeek4(userNumber) # recalling function