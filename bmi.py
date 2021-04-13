# Problem Task 01 (27/01/21)

# This program calculates a persons body mass index (BMI)
# from inputted height and weight

# Author: Caoimhin Vallely

# asks user to enter their weight and height
weight = float(input('Please enter your weight in kgs: '))
height = float(input('Please enter your height in cms: '))

# converts height in cm to metres
height_metres = height / 100

# formula for calculating BMI which is
# rounded to 2 decimal places
bmi = round(weight / (height_metres ** 2), 2)

# prints the result
print('Your bmi is ' + str(bmi))