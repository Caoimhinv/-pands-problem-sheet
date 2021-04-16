# Problem Task 07 (12/03/21)

# This program displays a plot of the functions f(x)=x, g(x)=x2 
# and h(x)=x3 in the range [0, 5] on the one set of axes. Resultant chart is saved as
# file plot_task_chart.png in this repositry

# Author: Caoimhin Vallely

# importing the NumPy library for the sums (creating and performing calculations on arrays) 
# and matplotlib.pyplot for the plot. 
# As per convention and economy of space I'm importing 
# these as 'np' and 'plt' respectively
import numpy as np
import matplotlib.pyplot as plt

# I'm setting the range on the x axis as [0,5] which will result in 0 to 4 which I think was
# the intention in the brief

# This creates a NumPy array in the range (0,5), i.e. 0 to 4. I only need to create this once.
xpoints = np.array(range(0, 5))
# f(x)=x interpreted as y = x
ypoints = xpoints
# Creates the first plot. I've formatted colour (c), label, marker type (o), marker size (ms), 
# marker edge colour(mec), marker face colour (mfc), line style (ls), line width (lw), transparency (alpha).
plt.plot(xpoints, ypoints, c = '#8B008B', label = "f(x)=x", marker = 'o', ms = 10, mew = 5,
    mec = 'cornflowerblue', mfc = 'lightcyan', ls = ':', lw = 2, alpha=0.75)

# g(x)=x2 interpreted as y = x squared
ypoints = (xpoints ** 2)
# Creates the second plot. Formatted elements as above with some variations
plt.plot(xpoints, ypoints, c = '#00008B', label = "g(x)=x^2", marker = 'o', ms = 10, mew = 5, 
    mec = 'indianred', mfc = 'gold', ls = '--', lw = 2, alpha=0.75)

# h(x)=x3 interpreted as y = x cubed
ypoints = (xpoints ** 3)
# Creates the third plot. Formatted elements as above with some variations
plt.plot(xpoints, ypoints, c = '#696969', label = "h(x)=x^3", marker = 'o', ms = 10, mew = 5,
    mec = 'rebeccapurple', mfc = 'hotpink', ls = '-.', lw = 2)

# Creating variables for font styles - type, colour, and size
font1 = {'family':'serif','color':'#696969','size':20}
font2 = {'family':'serif','color':'#00008B','size':15}

plt.title("Week 08 Plot Task", fontdict = font1, loc = 'left') # gives the plot a main title and 
                                                               # defines font style and positioning
plt.xlabel("x axis", fontdict = font2) # labels the x axis and specifies font style
plt.ylabel("y axis", fontdict = font2) # labels the y axis and specifies font style
plt.grid() # prints grid lines for ease of viewing intersections
plt.legend(loc = 'upper left') # prints the legend in the top left hand corner. Default 
                               # was top right which was obscuring some of the info
plt.xlim(-0.1,4.1) # extends the x axis a little bit either side so we can see the full markers clearly
plt.show() # prints the plot
