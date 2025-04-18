import matplotlib.pyplot as plt
import math
from math import e

freqArray = []
indexArray = []

for frequency in range(1,1000):
    freqArray.append(frequency)
    indexArray.append(math.sqrt(1+math.sqrt(1/(1.731-0.261*((frequency/(10**3))**2)))))

#Implementing the CIE colour matching algorithm based on the CIE 1931 colour model (although they spelt it color because they are american :O )
def freqToHexCode(f, n):
    c = 3*(10**8)

    #First convert the frequency to a wavelength
    wavelength = c / (n * f)

    #Then calculate the hue and saturation of the red-green axis ( X )
    if wavelength < 442:
        x1 = 0.0624 * (wavelength - 442)
    else:
        x1 = 0.0374 * (wavelength - 442)
    if wavelength < 599.8:
        x2 = 0.0264 * (wavelength - 599.8)
    else:
        x2 = 0.0323 * (wavelength - 599.8)
    if wavelength < 501:
        x3 = 0.0490 * (wavelength - 501.1)
    else:
        x3 = 0.0382 * (wavelength - 501.1)
    X = (0.362*e**((-0.5)*x1**2)) + (1.056*e**((-0.5)*x2**2)) - (0.065*e**((-0.5)*x3**2))

    #Then calculate the luminosity ( Y )
    if wavelength < 568.8:
        



plt.plot(freqArray, indexArray) #This plot a second line with these values alongside the first line.
plt.ylabel('Refractive Index')
plt.xlabel('frequency/THz')
plt.show()