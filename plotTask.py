# Problem Task 07 - Week08

# This program displays a plot of the functions f(x)=x, g(x)=x2 
# and h(x)=x3 in the range [0, 4] on the one set of axes.

# Author: Caoimhin Vallely

# importing NumPy for the sums (creating and performing calculations on arrays) 
# and matplotlib.pyplot for the plot. 
# As per convention and economy of space I'm importing 
# these as 'np' and 'plt' respectively
import numpy as np
import matplotlib.pyplot as plt

# I'm setting the range on the x axis from 0 to 3 - this seems implied in the way it is
# written in the brief - range [0,4] with a non-inclusive upper register.
# However the range function normally uses round brackets so was conflicted!

# This creates a NumPy array in the range (0,4), ie 0 to 3. I only need to create this once.
xpoints = np.array(range(0, 4))
# f(x)=x interpreted as y = x
ypoints = xpoints
# Creates the first plot. I've formatted colour (c), label, marker type (o), marker size (ms), 
# marker edge colour(mec), marker face colour (mfc), line style (ls), and line width (lw).
plt.plot(xpoints, ypoints, c = '#8B008B', label = "f(x)=x", marker = 'o', ms = 10, mew = 5,
    mec = 'cornflowerblue', mfc = 'lightcyan', ls = ':', lw = 2)

# g(x)=x2 interpreted as y = x squared
ypoints = (xpoints ** 2)
# Creates the second plot. Formatted elements as above with some variations
plt.plot(xpoints, ypoints, c = '#00008B', label = "g(x)=x^2", marker = 'o', ms = 10, mew = 5, 
    mec = 'indianred', mfc = 'gold', ls = '--', lw = 2) # creates the plot with some nice formatting

# h(x)=x3 interpreted as y = x cubed
ypoints = (xpoints ** 3)
# Creates the third plot. Formatted elements as above with some variations
plt.plot(xpoints, ypoints, c = '#696969', label = "h(x)=x^3", marker = 'o', ms = 10, mew = 5,
    mec = 'rebeccapurple', mfc = 'hotpink', ls = '-.', lw = 2) # creates the plot with some nice formatting

# Creating variables for font styles - type, colour, and size
font1 = {'family':'serif','color':'#696969','size':20}
font2 = {'family':'serif','color':'#00008B','size':15}

plt.title("Week 08 Plot Task", fontdict = font1, loc = 'left') # gives the plot a main title and 
                                                               # defines font style and positioning
plt.xlabel("x axis", fontdict = font2) # labels the x axis and specifies font style
plt.ylabel("y axis", fontdict = font2) # lables the y axis and specifies font style
plt.grid() # prints grid lines for ease of viewing intersections
plt.legend(loc = 'upper left') # prints the legend in the top left hand corner. Default 
                               # was top right which was obscuring some of the info
plt.xlim(0,3.1) # extends the x axis a little bit so we can see the full marker clearly
plt.show() # displays the plot
