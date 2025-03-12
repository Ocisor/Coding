import matplotlib.pyplot as plt

steps = 100
x = 0.9
k = 1.1
xVals = []


for i in range(steps):
    x = x + k - x**2
    xVals.append(x)


plt.plot(xVals, linestyle='-', color='b')
plt.xlabel('Step')
plt.ylabel('X Value')
plt.title('Data Points in xVals')
plt.show()