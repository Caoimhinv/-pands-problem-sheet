# Programming and Scripting - Weekly Tasks

## Caoimhin Vallely  

---

## Task 01 (27/01/21)
- **bmi.py**

### Task 
>*"Write a program that calculates a persons Body Mass Index (BMI). Call the file bmi.py. The inputs are the person's height in centimetres and weight in kilograms. The output is their weight divided by their height in metres squared."*

### Process
We start by using the built-in **input()** function to ask the user to enter their weight and height, which are then stored in 2 variables - **weight** and **height**. The brief asked for the input to be centimetres so I needed to convert the height variable to metres which I stored in another variable **height_metres**. We then enter each of the inputted values into the formula. The brief hinted that the answer should be rounded to 2 decimal places so I used the **round()** function to achieve that. The result is then printed.

### Code 

    weight = float(input('Please enter your weight in kgs?'))
    height = float(input('Please enter your height in cms?'))
    height_metres = height / 100
    bmi = round(weight / (height_metres ** 2), 2)
    print('Your bmi is ' + str(bmi))

### References
- variables - https://www.w3schools.com/python/python_variables.asp
- user input - https://www.w3schools.com/python/python_user_input.asp
- round - https://stackoverflow.com/questions/18781344/printing-a-variable-value-to-2-decimal-places  

---

## Task 02 (06/02/21)
- **secondString.py**

### Task 
>*"Write a program that asks a user to input a string and outputs every second letter in reverse order."*

### Process
We start by using the **input()** function to invite the user to enter a string sentence, which is stored in the variable **sentence**. We reverse the sentence by using a **slice** that steps backwards **[::-1]**, and store the result in the variable **sentence_reverse**. We then skip every second letter of this using a similar method **[::2]** and **print()** the result.

### Code
    
    sentence = input('Please enter a string sentence: ')
    sentence_reverse = sentence[::-1]
    print(sentence_reverse[::2])

### References 
- user input - https://www.w3schools.com/python/python_user_input.asp
- reversing string - https://www.w3schools.com/python/python_howto_reverse_string.asp
- returning every second letter of string - https://stackoverflow.com/questions/48873854/python-printing-ever-other-letter-of-a-word  

---

## Task 03 (11/02/21)
- **collatz.py**

### Task
>*"Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one."*

### Process
The first line of code asks the user to input a positive integer with the built in **input()** function. We use a **while** loop to firstly test **if** the number is even (modulo division (**%**) by two with 0 remainder), and if so, it gets divided by 2. If not (**else**) it gets multiplied by 3 and 1 added. The **while** loop only continues as long as the number is not equal (**!=**) to 1, at which point the program terminates ad the series of numbers is printed.  
This method didn't print the user's orginal number which seemed required in the brief, so I just added that in before the while loop with a simple **print** statement.

### Code 

    number = int(input("Please enter a positive integer: "))
    print(number)
    while (number != 1):
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        print(number)

### References 
- while loops - https://www.w3schools.com/python/python_while_loops.asp
- user input - https://www.w3schools.com/python/python_user_input.asp
- modulo operator - https://realpython.com/python-modulo-operator/  

---

## Task 04 (18/02/21)
- **weekday.py**

### Task
>*"Write a program that outputs whether or not today is a weekday."*

### Process
We begin by importing the **datetime** module. From within that, **datetime.today()** gives us the current day. The **weekday()** function lets us represent the days of the week as integers from 0-6 from Monday. So then, using a simple **if/else** condition, we see if the day of the week is less than 4 (Thursday or before), in which case it prints the statement *"Still a bloody weekday!! :("*. If it is 4, then I have a separate statement for Friday! Otherwise it has to be 5/6 so it prints *"Happy days it's the weekend!!! :)"*.

### Code 

    import datetime
    what_day_is_it = datetime.datetime.today().weekday()
    if what_day_is_it < 5:
        print ("Still a weekday!! :(")
    elif what_day_is_it == 4:
        print ("Still a weekday but we're very nearly there!!")
    else:
        print ("Happy days it's the weekend!!! :)")

### References  
- how to find if weekday or weekend - https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
- if/else - https://www.w3schools.com/python/python_conditions.asp  

---

## Task 05 (27/02/21)
- **squareRoot.py**

### Task  
>*"Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. You should create a function called <tt>sqrt</tt> that does this. I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x). This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots."*

### Process 
There were two separate challenges in this task - coming up with a theoretical solution to the brief, and then putting that into code.  
Newton's Method relies on the user guessing a number close to where they thought the square root lay, and then a few reiterations of the formula would narrow it down close enough to the actual answer. There was no mention of a second user input request in the brief, so I had to come with a workaround. I decided to use a random number, lower in value than the user unput, and just use enough iterations to narrow it down as close as I can. For the example given of 14.5, a few iterations would suffice, but for more extreme numbers a lot of iterations would be needed.  
I had a few attempts at this!  
I began by importing the **random** module which will let me initialise a random number to calculate against. A function which I named **sqrt()**, is then defined. The first element is the creation of the random number between 1 and the user's inputted number. This is generated by the **random.uniform()** function. This is stored in a variable **A**. My first effort involved running the user's inputted number and the random number **A** through the formula 100 times and **appending** all the results to a **list**. I'd then call the last element in the list as the result. On further investigation I realised I didn't need to store all of the results so I used the **x in range()** method to set up 100 iterations of the formula and return the last of these as the result. As pointed out by Andrew in his feedback, both these methods used up a lot of (unneccesary) memory. He also mentioned going to a precision. The latest version involves a **while** loop. This tests the difference in value between each iteration - the more the formula runs, the smaller the difference between each result - and if the difference falls below 0.001 we exit the function and return the result at that iteration. This certainly brings it to a precision but also only performs an absolutely necessary amount of calculation, and avoids excess use of memory. I was alerted to this method by a classmate and some quick research found the reference below on stackoverflow.com.

For the main program the user is asked to input a positive number which is converted to the type **float**. **If** it is negative, an error message is returned, otherwise the program carries on. The **user_number** is passed through the function **sqrt()**, and the result is then rounded to 1 decimal place as implied in the brief. The **rounded_result** is then printed out.

### Code 

    import random
    def sqrt(A):
        A = random.uniform(1, user_number)
        while True: 
            B = 0.5 * ((user_number / A) + A) 
            if (A - B) < 0.001: 
                return B
            A = B     

    user_number = float(input("Please enter a postive number: "))
    if user_number < 0: 
        print ("I said a positive number!!")
    else:
        result = sqrt(user_number)
        rounded_result = round(result, 1)
        print("The square root of ", user_number, "is approximately ", rounded_result) 

### References 
- Explanation of Newton's Method - https://www.school-for-champions.com/algebra/square_root_approx.htm#.YDuQ6i2l1pR
- functions - https://www.w3schools.com/python/python_functions.asp
- rounding numbers - https://www.w3schools.com/python/ref_func_round.asp
- random float - https://stackoverflow.com/questions/6088077/how-to-get-a-random-number-between-a-float-range
- range function - https://www.w3schools.com/python/ref_func_range.asp
- precision - https://stackoverflow.com/questions/20811208/newton-s-method-for-finding-square-roots-in-python  

---

## Task 06 (07/03/21)
- **es.py**
- **phadThai.txt**

### Task
>*"Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line."*

### Process
At the time of writing, a lot of this was new, so much research was required! The **sys** module seemed the most appropriate way to deal with arguments in the command line. **sys.argv[1]** allows 2 arguments in the command line - the program name and the filename or path. **'r'** lets us read the file and **'t'** specifies that it is text (as opposed to binary) - although this is probably unneccesary as both are the default values anyway.
So, if the textfile was in the same directory as the program, the user could enter the following directly into the command line:

    python es.py phadThai.txt

If the file was elsewhere, the filepath would be required, e.g.

    python es.py /Users/caoimhinvallely/Desktop/GMIT Weekly Tasks/Pands-problem-sheet/phadThai.txt

From here we're in more familiar territory - we **read()** the file, use the **count()** method to count the number of 'e's, and then **print()** the result.   
I updated this program after week 09 lectures on error handling and in particular **exceptions** which I thought might be appropriate. With the **try** condition the program behaves as expected if everything is entered correctly. The 2 **except** blocks only come into play if there's an error or **exception**. I've isolated the 2 most likely possibilities - 1. incorrect/misspelt filename or path, i.e. the program doesn't recognise or can't find the inputted file. 2. no filename entered at all. After a bit of research I found these exceptions to be **IOError** and **IndexError**. If either of these are raised a helpful bit of advice is printed.  
I've included a txt file in the repositry called **phadThai.py** to test the program, although any txt file will work once the correct path is inputted.

### Code
    
    import sys
    try: 
        with open(sys.argv[1], 'rt') as text_file:                       
            contents = text_file.read() 
            number_of_es = contents.count("e") 
            print ("There are {} 'e's in this file".format(number_of_es))
    except IOError: 
        print("I can't seem to find your file? If it's in the same folder just enter <<filename.txt>>, if it's elsewhere enter the full path.")
    except IndexError:
        print("Did you enter a file in the command line? Input should be 'python es.py filename.txt'")

### References
- file handling - https://www.w3schools.com/python/python_file_handling.asp
- sys.argv[] - https://www.pythonforbeginners.com/system/python-sys-argv
- try/except - https://www.w3schools.com/python/python_try_except.asp
- IOError - https://www.tutorialspoint.com/How-to-catch-IOError-Exception-in-Python#:~:text=It%20is%20an%20error%20raised,for%20operating%20system%2Drelated%20errors.
- IndexError - https://airbrake.io/blog/python/python-indexerror  

---

## Task 07 (12/03/21)
- **plotTask.py**
- **plotTask.png**

### Task
>*"Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. Some marks will be given for making the plot look nice."*

### Process
A big clue was given in the weekly labs so the coding element of this was straight forward enough. I spent most of my time having fun with the formatting possibilities! If this was an important bit of data for presentation I would obviously have toned it down a little and focused on the clearest way to present and visualise the data. Here I took the opportunity to try out colours, line style, linesize, markers, marker formatting, label formatting and positioning.        
We begin by importing the **NumPy** library which allows us to perform calculations on an entire array, and **matplotlib.pyplot** lets us draw the plots. These are imported as **np** and **plt** respectively.
We then create a **numpy.array** with the **range** (0,5) on the x axis. This will result in values from 0 to 4, as the upper trange is non-inclusive. I felt this was implied in the wording of the brief as opposed to the range being [0,4] which would result in the values from 0 to 3 only.
I worked out the code for each of the formulas and then formatted the following plot elements:  

- c = line colour
- label = name/label of data
- marker = marker at integer intersections
- ms = marker size
- mew = marker edge width
- mec = marker edge colour
- mfc = marker face colour
- ls = line style
- lw = line width
- alpha = transparency (markers, lines, etc.)

I've included all the various labels, heading, and legend, also with some formatting, plus incorporated a grid (**plt.grid()**) for ease of reading the results. **plt.xlim(-0.1,4.1)** increases the range of the x axis slightly so the markers on **0** and **4** are completely visible.  
I've saved a **png** file of the resultant plot in the repositry - **plot_task_chart.png**

### Code

    import numpy as np
    import matplotlib.pyplot as plt

    xpoints = np.array(range(0, 5))

    ypoints = xpoints
    plt.plot(xpoints, ypoints, c = '#8B008B', label = "f(x)=x", marker = 'o', 
    ms = 10, mec = '#FFE4C4', mfc = '#FFE4C4', ls = ':', lw = 2, alpha=0.75)

    ypoints = (xpoints ** 2)
    plt.plot(xpoints, ypoints, c = '#00008B', label = "g(x)=x^2", marker = 'o', 
    ms = 10, mec = '#7FFFD4', mfc = '#7FFFD4', ls = '--', lw = 2, alpha=0.75)

    ypoints = (xpoints ** 3)
    plt.plot(xpoints, ypoints, c = '#696969', label = "h(x)=x^3", marker = 'o', 
    ms = 10, mec = 'hotpink', mfc = 'hotpink', ls = '-.', lw = 2)

    font1 = {'family':'serif','color':'#696969','size':20}
    font2 = {'family':'serif','color':'#00008B','size':15}

    plt.title("Week 08 Plot Task", fontdict = font1, loc = 'left') 
    plt.xlabel("x axis", fontdict = font2)
    plt.ylabel("y axis", fontdict = font2)
    plt.grid()
    plt.legend(loc = 'upper left')
    plt.xlim(-0.1,4.1)
    plt.show() 

### References
- matplotlib - https://www.w3schools.com/python/matplotlib_intro.asp
- numpy - https://www.w3schools.com/python/numpy_intro.asp
- colours - https://matplotlib.org/stable/tutorials/colors/colors.html  
- aplha/transparency - http://www.learningaboutelectronics.com/Articles/How-to-change-the-transparency-of-a-graph-plot-in-matplotlib-with-Python.php  

---
# ***THE END***