# Pands Weekly Problem Sheets - Caoimhin Vallely

---

## Task 01 - Week 02 (27/01/21)

### Task 
>*"Write a program that calculates a persons Body Mass Index (BMI). Call the file bmi.py. The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared."*

### Issues
- convert cms to metres
- formula for calculating BMI
- rounding up to 2 decimal places

### Process
???

### Code 

    height_metres = height / 100
    bmi = round(weight / (height_metres ** 2), 2)
    print('Your bmi is ' + str(bmi))

### References
- round - https://stackoverflow.com/questions/18781344/printing-a-variable-value-to-2-decimal-places

---

## Task 02 - Week 03 (06/02/21)

### Task 
>*"Write a program that takes asks a user to input a string and outputs every second letter in reverse order."*

### Issues 
- functions for reversing string and for printing out every second letter

### Process
???

### Code
    
    sentence = input('Please enter a string sentence: ')
    sentenceReverse = sentence[::-1] # reverses the sentence
    sentenceSkip = sentenceReverse[::2] # prints every second letter
    print(sentenceSkip)

### References 
- reversing string - https://www.w3schools.com/python/python_howto_reverse_string.asp
- returning every second letter of string - https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word

---

## Task 03 - Week04 (11/02/21)

### Task
>*"Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one."*

### Issues
- Testing for number being even
- While loop

### Process
???

### Code 

    number = int(input("Please enter a positive integer: "))

    while (number != 1):
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        print(number)

### References 
- while loops - https://www.w3schools.com/python/python_while_loops.asp
- user inputing - https://www.w3schools.com/python/python_user_input.asp

---

## Task 04 - Week 05 (18/02/21)

### Task
>*"Write a program that outputs whether or not today is a weekday."*

### Issues 
- finding out what day it is
- how to differentiate between weekday and weekend efficiently

### Process
We being by importing the **datetime** module. Within that, **datetime.today()** gives us the day today. The **weekday()** method lets us represent the days of the week as integers from 0-6 from Monday. So then we use a **while** loop, where if the day of the week is less than 5 (Friday or before), it prints the statement *"Still a bloody weekday!! :("*. Otherwise it prints *"Praise the lord it's the weekend!!! :)"*.

### Code 

    import datetime

    whatDayIsIt = datetime.datetime.today().weekday()

    if whatDayIsIt < 5:
        print ("Still a weekday!! :(")
    else:
        print ("Praise the lord it's the weekend!!! :)")

### References  
- how to find if weekday or weekend - https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
- if/else - https://www.w3schools.com/python/python_conditions.asp

---

## Task 05 - Week 06 (27/02/21)

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
Newton's Method relies on the user guessing a number close to where they thought the square root lay, and then a few reiterations of the formula would narrow it down. There was no mention of a second user input request in the brief so I had to come with a workaround. I decided to use the **random.uniform()** module to choose a random floating point number between 1 and the user's inputted number, and then just using enough iterations to narrow it down. For the example given of 14.5, a few iterations would suffice, but for more extreme numbers a lot of iterations would be needed.  
So using a **while** loop I settled on 100 iterations which seemed to cater for any number I could think of within reason! This could obviously be increased if really necessary.
The results are stored in a **list** within the function. When the function **sqrt()** is called we only need the last entry in the list which we **round()** to 1 decimal place as seems implied in the brief.

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

---

## Task 06 - Week 07 (07/03/21)

### Task
>*"Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line."*

### Issues
- accessing and reading the text file
- counting the number of e's

### Process
At the time of writing, a lot of this was new, so research was required! The **sys** module seemed the most appropriate way to deal with arguments in the command line. **sys.argv[1]** allowed 2 arguments in the command line - the programme/script (es.py) and the filename (e.g. phadThai.txt). **'r'** lets us read the file and **'t'** specifices that it is text (as opposed to binary) - although this is probably unneccesary as both are the default values anyway.
The user would enter into the command line:

    `python es.py phadThai.txt`

From here we're on more familiar territory - we **read()** the file, use the **count()** method to count the number of 'e's, and then **print()** the result.

### Code
    
    import sys
    with open(sys.argv[1], 'rt') as textFile:
    contents = textFile.read() 
    numberOfEs = contents.count("e") 
    print ("There are {} 'e's in this file".format(numberOfEs))

### References
- file handling - https://www.w3schools.com/python/python_file_handling.asp
- sys.argv[] - https://www.pythonforbeginners.com/system/python-sys-argv

---

## Task 07 - Week 08 (12/03/21)

### Task
>*"Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. Some marks will be given for making the plot look nice."*

### Issues
- interpreting the formulas
- formatting the plot

### Process
A big clue was given in the weekly labs so the coding element of this was straight forward enough. I spent most of my time exploring the formatting possibilities! If this was an important bit of data for presentation I would obviously have toned it down and focused on the clearest way to present and visualise the data. Here I took the opportunity to try out colours, line style, linesize, markers, marker formatting, label formatting and positioning.

### Code

    import numpy as np
    import matplotlib.pyplot as plt

    xpoints = np.array(range(0, 4))

    ypoints = xpoints
    plt.plot(xpoints, ypoints, c = '#8B008B', label = "f(x)=x", marker = 'o', ms = 10, mec = '#FFE4C4', mfc = '#FFE4C4', ls = ':', lw = 2)

    xpoints = np.array(range(0, 4))
    ypoints = (xpoints ** 2)
    plt.plot(xpoints, ypoints, c = '#00008B', label = "g(x)=x^2", marker = 'o', ms = 10, mec = '#7FFFD4', mfc = '#7FFFD4', ls = '--', lw = 2)

    xpoints = np.array(range(0, 4))
    ypoints = (xpoints ** 3)
    plt.plot(xpoints, ypoints, c = '#696969', label = "h(x)=x^3", marker = 'o', ms = 10, mec = 'hotpink', mfc = 'hotpink', ls = '-.', lw = 2)

    font1 = {'family':'serif','color':'#696969','size':20}
    font2 = {'family':'serif','color':'#00008B','size':15}

    plt.title("Week 08 Plot Task", fontdict = font1, loc = 'left') 
    plt.xlabel("x axis", fontdict = font2)
    plt.ylabel("y axis", fontdict = font2)
    plt.grid()
    plt.legend(loc = 'upper left')
    plt.show() 

### References
- matplotlib - https://www.w3schools.com/python/matplotlib_intro.asp
- numpy - https://www.w3schools.com/python/numpy_intro.asp

---
# THE END