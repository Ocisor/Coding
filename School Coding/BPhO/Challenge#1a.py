import matplotlib.pyplot as plt
from math import e # Eulers number :O
import math
def refractiveIndex():
    #Constants
    c = 3 * (10**8)
    #coefficients from https://refractiveindex.info/?shelf=3d&book=glass&page=BK7 under the Dispersion Formula Tab
    a = [1.03961212, 0.231792344, 1.01046945]
    b = [0.00600069867, 0.0200179144, 103.560653]
    nValues = []
    λValues = []
    for i in range(380, 750, 10):
        λ = i/1000
        summation = 0
        for j in range(3):
            summation += (a[j]*λ*λ)/((λ**2)-b[j])
        nValues.append(math.sqrt(1+summation))
        λValues.append(i)
    return nValues, λValues

n,λ = refractiveIndex()
plt.plot(λ, n) #This plot a second line with these values alongside the first line.
plt.ylabel('n')
plt.xlabel('λ /nm')
plt.show()