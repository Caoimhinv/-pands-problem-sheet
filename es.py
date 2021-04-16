# Problem Task 06 (07/03/21)

# This program reads in a text file in the command line
# and outputs the number of 'e's contained in it.

# Author: Caoimhin Vallely

# The user types in the programme name and filename or filepath 
# directly into the command line
# i.e. >>python es.py phadThai.txt<<
# N.B. text file needs to be in the same folder as program
# or else the full filepath is required.
# I've included phadThai.txt in the reposity here as an example text file

# importing the sys module to handle arguments in the command line
import sys

try: # Error handling - I'm including this to mitigate against incorrect entries in the command line.
     # Might be just me but I think this could be a common issue! 

    with open(sys.argv[1], 'rt') as text_file: # sys.argv[1] refers to the 2nd argument in the command line,
                                         # i.e. the 1st [0] would have been the program (es.py) and 2nd [1]
                                         # is the filename (e.g. phadThai.txt)
                                         # 'rt' lets us 'read' the file and specifices 'text' as opposed to binary.
                                         # File is stored as 'textfile'
        contents = text_file.read() # this reads the content of the file and stores it in the variable 'contents'
        number_of_es = contents.count("e") # uses 'count' method to count number of "e"s.
                                    # I'm assuming that it's just lower case 'e' that is required
                                    # although including capital 'E' would be quite straightforward.
        print ("There are {} 'e's in this file".format(number_of_es)) # prints the result
 
# exceptions 
except IOError: # catches if incorrect file name or path entered, and the following is printed
    print("I can't seem to find your file? If it's in the same folder just enter <<filename.txt>>, if it's elsewhere enter the full filepath.")
except IndexError: # catches if no file at all is entered, and the following is printed
    print("Did you enter a file in the command line? Input should be 'python es.py filename.txt'")
