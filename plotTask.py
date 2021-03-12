# Week 08 Weekly Problem Task
# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Caoimhin Vallely

# importing numpy for the sums and matplotlib for the visuals
import numpy as np
import matplotlib.pyplot as plt

# sets the range on the x axis from 0 to 4
xpoints = np.array(range(0, 4))

# f(x)=x interpreted as y = x
ypoints = xpoints
plt.plot(xpoints, ypoints, c = '#8B008B', label = "f(x)=x", marker = 'o', ms = 10, mec = '#FFE4C4', mfc = '#FFE4C4', ls = ':', lw = 2) # creates the plot with some nice formatting

# g(x)=x2 interpreted as y = x squared
xpoints = np.array(range(0, 4))
ypoints = (xpoints ** 2)
plt.plot(xpoints, ypoints, c = '#00008B', label = "g(x)=x^2", marker = 'o', ms = 10, mec = '#7FFFD4', mfc = '#7FFFD4', ls = '--', lw = 2) # creates the plot with some nice formatting

# h(x)=x3 interpreted as y = x cubed
xpoints = np.array(range(0, 4))
ypoints = (xpoints ** 3)
plt.plot(xpoints, ypoints, c = '#696969', label = "h(x)=x^3", marker = 'o', ms = 10, mec = 'hotpink', mfc = 'hotpink', ls = '-.', lw = 2) # creates the plot with some nice formatting

# playing with fonts
font1 = {'family':'serif','color':'#696969','size':20}
font2 = {'family':'serif','color':'#00008B','size':15}

plt.title("Week 08 Plot Task", fontdict = font1, loc = 'left') # gives the plot an overall title
plt.xlabel("x axis", fontdict = font2) # labels the x axis
plt.ylabel("y axis", fontdict = font2) # lables the y axis
plt.grid() # prints grid lines
plt.legend(loc = 'upper left') # prints the legend in the top left hand corner. Default was top right which was obscuring some of the info
plt.show() # displays the plot
