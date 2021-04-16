# Problem Task 03 (11/02/21)

# This program asks the user to input any positve integer.
# At each step it calculates the next value 
# by taking the current value and, if it is even,
# divides it by two, but if it is odd, 
# multiplies it by three and adds one.
# The program ends if the current value is one.

# Author: Caoimhin Vallely

# asks the user to enter a number which is converted to an integer and stored in the variable 'number'
number = int(input("Please enter a positive integer: "))

# the while loop
print(number) # example given in the brief suggests the user number should be printed first
while (number != 1): # stops program when number hits 1
    if number % 2 == 0: # checks if number is even 
        number = number // 2 # if so, divides it by 2
    else:
        number = (number * 3) + 1 # if not, multiplies it by 3 and adds 1
                                  # Program loops until we reach 1 
    print(number) # prints the result