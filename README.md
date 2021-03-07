# Pands Weekly Problem Sheets

## Weekly task 2 (27/01/21)

### Task 
>*"Write a program that calculates a persons Body Mass Index (BMI). Call the file bmi.py. The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared."*

### Issues
- convert cms to metres
- formula for calculating BMI
- rounding up to 2 decimal places

### Code 

    height_metres = height / 100
    bmi = round(weight / (height_metres ** 2), 2)
    print('Your bmi is ' + str(bmi))

### References
- 2 decimal places - https://stackoverflow.com/questions/18781344/printing-a-variable-value-to-2-decimal-places

## Weekly task 3 (06/02/21)

### Task 
>*"Write a program that takes asks a user to input a string and outputs every second letter in reverse order."*

### Issues 
- functions for reversing string and for printing out every second letter

### Code
    
    sentence = input('Please enter a string sentence: ')
    sentenceReverse = sentence[::-1] # reverses the sentence
    sentenceSkip = sentenceReverse[::2] # prints every second letter
    print(sentenceSkip)

### References 
- reversing string - https://www.w3schools.com/python/python_howto_reverse_string.asp
- returning every second letter of string - https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word

## Weekly task 4 (11/02/21)

### Task
>*"Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one."*

### Issues
- Testing for number being even
- While loop

### Code 

    number = int(input("Please enter a positive integer: "))

    while (number != 1):
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        print(number)

### References 
-

## Weekly task 5 (18/02/21)

### Task
>*"Write a program that outputs whether or not today is a weekday."*

### Issues 
- finding out what day it is
- how to differentiate between weekday and weekend efficiently

### Code 

    import datetime

    whatDayIsIt = datetime.datetime.today().weekday()

    if whatDayIsIt < 5:
        print ("Still a weekday!! :(")
    else:
        print ("Praise the lord it's the weekend!!! :)")

### References  
- how to find if weekday or weekend - https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python

## Weekly Task 6 (27/02/21)

### Task  
>*"Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called <tt>sqrt</tt> that does this. I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots."*

### Issues
- Create a function to calculate square root from user input using Newton's method
- Create a random number to use for calculation
- reiterate calculation and put results in a list
- return the last value from that list
- round the number to 1 decimal point

### Process 
There were two separate challenges in this task - coming up with a theoretical solution to the brief, and then putting that in code.
Newton's Method relies on the user guessing a number close to where they thought the square root lay, and then a few reiterations of the formula would narrow it down. There was no mention of a second user input request in the brief so I had to come with a workaround. I decided to use the random uniform module to choose a random floating point number between 1 and the user's inputted number, and then just using enough iterations to narrow it down. For the example given of 14.5, a few iterations would suffice, but for more extreme numbers a lot of iterations would be needed.  
So using a while loop I settled on 100 iterations which seemed to cater for any number I could think of within reason! This could obviously be increased if really necessary.
I created a list within the function to store the results, although it's only the last item in the list I actually need.

### Code 

    import random

    def sqrt():
        L=[]
        global number
        number = float(input("Enter a postive number: "))
        A = random.uniform(1, number)
        while len(L) < 100:
            A = 0.5 * ((number / A) + A)
            L.append(A)
        return L

    result = sqrt()
    roundedResult = round(result[99], 1)
    print("The square root of ", number, "is approximately ", roundedResult)

### References 
- Explanation of Newton's Method - https://www.school-for-champions.com/algebra/square_root_approx.htm#.YDuQ6i2l1pR
- while loop - https://www.w3schools.com/python/python_while_loops.asp
- list - https://www.w3schools.com/python/python_lists.asp
- functions - https://www.w3schools.com/python/python_functions.asp
- rounding numbers - https://www.w3schools.com/python/ref_func_round.asp
- random float - https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range

## Weekly Task 7 (07/03/21)

### Task
>*"Write a program that reads in a text file and outputs the number of e's it contains.

>The program should take the filename from an argument on the command line."*

### Issues
???

### Process
???

### Code
    
    import sys
    with open(sys.argv[1], 'r') as textFile:
    contents = textFile.read() 
    numberOfEs = contents.count("e") 
    print ("There are {} 'e's in this file".format(numberOfEs))

### References
