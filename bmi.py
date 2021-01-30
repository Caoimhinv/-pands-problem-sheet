# calculate BMI from inputted height and weight
# Author: Caoimhin Vallely

# ask user to enter their info
weight = float(input('Please enter your weight in kgs?'))
height = float(input('Please enter your height in cms?'))

# adapted formula (cms) for calculating BMI and rounded to 2 decimal places
bmi = round(weight / (height ** 2) * 10000, 2)

print('Your bmi is ' + str(bmi))