# Given: "Write a program that reads in a text file and outputs the number of 'e's 
# it contains. The program should take the filename from an argument on 
# the command line."

# Author: Caoimhin Vallely

# User types in programme name and file name in the command line
# i.e. >>python es.py phadThai.txt<<
# N.B. text file needs to be in the same folder as program
# I've included phadThai.txt here as an example text file

# importing the sys module for accessing the text file
import sys

# accesses and allows the programme to 'read' the text file from the command line
try: # Error handling - I'm including this to mitigate against incorrect entries into the command line.
     # Might be just me but I think this could be a common issue! 
    with open(sys.argv[1], 'rt') as textFile: # sys.argv[1] refers to 2 arguments in the command line,
                                         # i.e. 1. programme (es.py) and 2. filename (e.g. phadThai.txt) or file path
                                         # (e.g /Users/caoimhinvallely/Desktop/GMIT Weekly Tasks/Pands-problem-sheet/phadThai.txt)
                                         # 'rt' lets us 'read' the file and specifices 'text' as opposed to binary
        contents = textFile.read() # reads the content of the file and stores it in a variable 'contents'
        numberOfEs = contents.count("e") # uses 'count' method to count number of "e"s.
                                    # I'm assuming that it's just lower case 'e' that is required
                                    # although including capital 'E' would be quite straightforward.
        print ("There are {} 'e's in this file".format(numberOfEs)) # prints the result
        #print (sys.argv) # prints the arguments in the command line
except IOError: # catches if incorrect file name or path entered, and the following printed
    print("I can't seem to find your file? If it's in the same folder just enter <<filename.txt>>, if it's elsewhere enter the full path.")
except IndexError: # catches if no file at all entered, and the following printed
    print("Did you enter a file in the command line? Input should be 'python es.py filename.txt'")
