import matplotlib.pyplot as plt

A, B, C, F = 0, -0.1, 0.1, 0
timeStep = 0.01
STEPS = 3000
x, y = int(input("Starting X value: ")), int(input("Starting Y value: ") )
x_values = [0] * STEPS
y_values = [0] * STEPS

for day in range(STEPS):
    x_values[day] = x + (((A*x)-(B*x*y))*timeStep)
    y_values[day] = y + (((C*x*y)-(F*y))*timeStep)
    x = x_values[day]
    y = y_values[day]

print(((A+F)*(A+F)-4*(A*F-B*C)) > 0)
print(x_values,y_values)
plt.scatter(x_values,y_values)
plt.show()