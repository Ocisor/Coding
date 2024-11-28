import matplotlib.pyplot as plt

A, B, C, F = 1.2, 0.5, 0.5, 0.2
timeStep = 0.01
STEPS = 1000
x, y = int(input("Starting X value: ")), int(input("Starting Y value: ") )
x_values = [0] * STEPS
y_values = [0] * STEPS

for day in range(STEPS):
    x_values[day] = x + (((A*x)-(B*x*y))*timeStep)
    y_values[day] = y + (((C*x*y)-(F*x))*timeStep)
    x = x_values[day]
    y = y_values[day]

plt.scatter(x_values,y_values)
plt.show()