# calculate BMI from inputted height and weight
# Author: Caoimhin Vallely

# asks user to enter their info
weight = float(input('Please enter your weight in kgs?'))
height = float(input('Please enter your height in cms?'))

# converts height in cm to metres
height_metres = height / 100

# formula for calculating BMI and rounds to 2 decimal places
bmi = round(weight / (height_metres ** 2), 2)

# prints the result
print('Your bmi is ' + str(bmi))