# Given: "Write a program that reads in a text file and outputs the number of 'e's 
# it contains. The program should take the filename from an argument on 
# the command line."

# Author: Caoimhin Vallely

# User types in programme name and file name in the command line
# i.e. >>python es.py phadThai.txt<<
# N.B. text file mneeds to be in the same folder as programme
# I've included phadThai.txt here as an example text file

# importing the sys module for accessing the text file
import sys

# accesses and allows the programme to 'read' the text file from the command line
with open(sys.argv[1], 'rt') as textFile: # sys.argv[1] refers to 2 arguments in the command line,
                                         # i.e. 1. programme (es.py) and 2. filename (e.g. phadThai.txt)
                                         # 'rt' lets us 'read' the file and specifices 'text' as opposed to binary
    contents = textFile.read() # reads the content of the file
    numberOfEs = contents.count("e") # uses 'count' method to count number of "e"s.
                                    # I'm assuming that it's just lower case 'e' that is required
                                    # although including capital 'E' would be quite straightforward.
    print ("There are {} 'e's in this file".format(numberOfEs)) # prints the result