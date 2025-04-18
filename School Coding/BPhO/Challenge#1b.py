import matplotlib.pyplot as plt
import math

def determineColour(f): # f for frequency
    if f < 405:
        colour_str = 'Infra Red'
    elif (f>=405) and ( f < 480 ):
        colour_str = 'Red'
    elif (f>=480) and ( f < 510 ):
        colour_str = 'Orange'
    elif (f>=510) and ( f < 530 ):
        colour_str = 'Yellow'
    elif (f>=530) and ( f < 600 ):
        colour_str = 'Green'
    elif (f>=600) and ( f < 620 ):
        colour_str = 'Cyan'
    elif (f>=620) and ( f < 680 ):
        colour_str = 'Blue'
    elif (f>=680) and ( f <= 790 ):
        colour_str = 'Violet'
    else:
        colour_str = 'Ultra Violet'

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
    if wavelength < 442:
        x1 = 0.0624 * (wavelength - 442)
    else:
        x1 = 0.0374 * (wavelength - 442)
    x2
    x3



plt.plot(freqArray, indexArray) #This plot a second line with these values alongside the first line.
plt.ylabel('Refractive Index')
plt.xlabel('frequency/THz')
plt.show()