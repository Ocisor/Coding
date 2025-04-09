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
    nValues = []
    λValues = []
    for i in range(1486000,1527700,417):
        n = i/1000000
        λ = math.sqrt(((n**n)-1)/(combinedCoef))
        nValues.append(n)
        λValues.append(λ)
    return nValues, λValues

n,λ = refractiveIndex()

plt.plot(n,λ) #This plot a second line with these values alongside the first line.
plt.ylabel('n')
plt.xlabel('λ /nm')
plt.show()