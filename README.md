# Weather-Data-Plots

There are two files for this assignment.
• pretty_plot.py
• plotting_data.py

This assignment is meant to help gain familiarity with two of the most commonly used engineering packages in Python: numpy and matplotlib.

Activity #1: Pretty plot – individual
The program named pretty_plot.py  repeatedly multiplies a matrix by a point and plots the results.

Starts with a 2D point, (𝑥, 𝑦). This point can be represented as a vector: 𝑣 = [𝑥 𝑦]. There is also defined a 2x2 matrix, 𝑀 = [𝑎 𝑏 𝑐 𝑑]. Computing the product of 𝑀 with 𝑣 will give a new point 𝑣′: 𝑣′ = 𝑀𝑣. Then, multiply the matrix 𝑀 by the new point 𝑣′, to get another point, i.e. 𝑣′′ = 𝑀𝑣′. This can go on indefinitely, creating a long sequence of points.

The program should use numpy to create a matrix and a point. Begin with the point (0, 1) and the matrix: [ 1.02 0.095 −0.095 1.02 ]. Then, multiply the matrix by the point to get a new point. Repeat for a total of 250 times. The program plots the data points using matplotlib. Be sure to label the x and y axes, and include a title.

Note: the purpose of this activity is to get practice with numpy.

Activity #2: Plotting data

The program named plotting_data.py reads in weather data from the file WeatherDataCLL.csv and plots the data in a set of graphs described below. Using matplotlib, this program creates the following 4 graphs (on separate plots).
  1) A line graph that shows both the maximum temperature and average wind speed plotted over the period of time. Both lines should be plotted on the same               graph, with date on the x-axis, and different y axes for the two different measurements. (Please do not spend time dealing with “date data type.” Please just       consider the dates in the data to be strings, or, you may simply consider the days as integers for plotting.)
  2) A histogram of the average wind speed. The x axis should cover a reasonable range of average wind speeds, and the y axis should show the number of days             that had an average wind speed in the specific range.
  3) A scatterplot indicating the relationship (or lack thereof) between precipitation and average relative humidity (one on each axis).
  4) A bar chart, with one bar per calendar month (each month from all 10 years), showing the average temperature, along with lines indicating the highest               high and lowest low temperatures from that month.
