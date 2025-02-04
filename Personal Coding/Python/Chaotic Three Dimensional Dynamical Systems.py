# Evolution of the Lorenz attractor
#
# The equations we are solving are
# dx = a (y - x)
# dy = x (r - z) - y
# dz = xy - bz
#
# Art Mountain 2025
import matplotlib.pyplot as plt
from matplotlib import animation

nPoints = 2500

# lists to store x, y and z points
t, xdata, ydata, zdata = [], [], [], []

# Fill in evaluation of Lorentz system here
x = int(input(f"input starting x value."))
y = int(input(f"input starting y value."))
z = int(input(f"input starting z value."))
a = 100
b = 28
c = 8/3
dt = 0.01
for i in range(int(input("How many steps?"))):
    dx = a*(y-x)*dt
    dy = (x*(b-z)-y)*dt
    dz = (x*y-c*z)*dt
    x += dx
    y += dy
    z += dz
    xdata.append(x)
    ydata.append(y)
    zdata.append(z)

plt.style.use('dark_background')
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)
plt.title('Lorenz attractor')

# Set the axes to be the min to the max of each variable to fit the axes to the plot
ax.set_xlim3d([min(xdata), max(xdata)])
ax.set_xlabel('X')
ax.set_ylim3d([min(ydata), max(ydata)])
ax.set_ylabel('Y')
ax.set_zlim3d([min(zdata), max(zdata)])
ax.set_zlabel('Z')

line, = ax.plot([], [], [], lw=2)


def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,


def animate(i):
    line.set_data(xdata[:i], ydata[:i])
    line.set_3d_properties(zdata[:i])
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nPoints, interval=1,
                               repeat_delay=5, blit=True)
plt.show()

# Uncomment to save the animation as gif video file
anim.save('C:/Users/jbamf/OneDrive/Desktop/Blender/Renders/LorenzAttractor.gif', writer=animation.PillowWriter(fps=20))
