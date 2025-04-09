import matplotlib.pyplot as plt
from math import e # Eulers number :O
import math
def refractiveIndex():
    #Constants
    c = 3 * (10**8)
    #coefficients from https://refractiveindex.info/?shelf=3d&book=glass&page=BK7 under the Dispersion Formula Tab
    a1 = 1.03961212
    a2 = 0.231792344
    a3 = 1.01046945
    b1 = 0.00600069867
    b2 = 0.0200179144
    b3 = 103.560653
    combinedCoef = (a1/(1-b1))+(a2/(1-b2))+(a3/(1-b3))
    values = []
    λ = math.sqrt(((n**n)-1)/(combinedCoef))
    
    for i in range(1527700,1486000,-417):
        print(i)
        #n = i/1000000
        #λ = math.sqrt(((n**n)-1)/(combinedCoef))
        #values.append([n,λ])
    print(values)

refractiveIndex()
#plt.plot([1, 2, 3, 4]) #Automatically assumes these are y values. Add a second array for x values
#plt.plot(1,2) #This plot a second line with these values alongside the first line.
#plt.ylabel('n')
#plt.xlabel('λ /nm')
#plt.show()