import matplotlib.pyplot as plt
from math import e # Eulers number :O

xVals = []
yVals = []

for y in range(100):
    yVals.append(e**(0.5*y)) 
    xVals.append(y)

plt.plot([1, 2, 3, 4]) #Automatically assumes these are y values. Add a second array for x values
plt.plot(yVals, xVals) #This plot a second line with these values instead.
plt.ylabel('some numbers')
plt.show()