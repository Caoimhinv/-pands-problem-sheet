# Calculate someones BMI from height and weight
# Author: Caoimhin Vallely

# ask user to enter their info
weight = float(input('Please enter your weight in kgs?'))
height = float(input('Please enter your height in cms?'))

bmi = weight / (height ** 2) * 10000
#round to 2 decimal places
bmiTwoDecimalPlaces = round(bmi, 2)

print('Your bmi is ' + str(bmiTwoDecimalPlaces))