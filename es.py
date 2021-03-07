# importing the sys module for accessing the text file
import sys

# open the text file from the command line
with open(sys.argv[1], 'r') as textFile:
    contents = textFile.read() # reads the content of the file
    numberOfEs = contents.count("e") # count method to count number of "e"s
    print ("There are {} 'e's in this file".format(numberOfEs)) # prints the result