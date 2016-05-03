import graph_data
import matplotlib.pyplot as pyplot

axis_data = [i for i in range(100)] # the numbers 0 to 99
xdata = graph_data.xdata # some random numbers
ydata = graph_data.ydata # other random numbers

pyplot.plot(axis_data, xdata)
pyplot.plot(axis_data, ydata)
pyplot.savefig('example.png')
