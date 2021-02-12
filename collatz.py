# This program asks the user to input any positve integer
# At each step it calculates the next value 
# by taking the current value and, if it is even,
# divides it by two, but if it is odd, 
# multiplies it by three and adds one.
# The program ends if the current value is one.

# Author: Caoimhin Vallely

number = int(input("Please enter a positive integer: ")) # asks user to enter number

while (number != 1): # stops program when number hits 1
    if number % 2 == 0: # checking if number is even 
        number = number // 2 # dividing by 2
    else:
        number = number * 3 + 1 # if not even, multiplying by 3 and adding 1
    print(number)