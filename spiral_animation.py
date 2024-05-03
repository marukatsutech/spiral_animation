# Spiral animation
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d


def change_k(value):
    global k
    k = float(value)


def change_o(value):
    global omega
    omega = float(value)


def set_axis():
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)
    ax.set_title('Spiral')
    ax.set_xlabel('x * pi')
    ax.set_ylabel('y')
    ax.set_zlabel('z * i')
    ax.grid()


def update(f):
    ax.cla()  # Clear ax
    set_axis()
    ax.text(x_min, y_max, z_max * 0.9, "Step(as t)=" + str(f))
    ax.text(x_min, y_max, z_max * 0.7, "k=" + str(f'{k:.2f}') + ", omega=" + str(f'{omega:.2f}'))
    # Draw a circle
    c = Circle((0, 0), 1, ec='gray', fill=False)
    ax.add_patch(c)
    art3d.pathpatch_2d_to_3d(c, z=0, zdir="x")
    # Draw a center line
    line = art3d.Line3D([x_min, x_max], [0, 0], [0, 0], color='gray', ls="-.", linewidth=1)
    ax.add_line(line)
    # Draw sine wave
    y = np.sin((k * x - omega * f) * np.pi)  # Note: math.pi for adjustment x axis as x * pi
    ax.plot(x, y, z_min, color='gray', ls="-", linewidth=1)
    # Draw cosine wave
    y = x * 0. + y_max
    z = np.cos((k * x - omega * f) * np.pi)  # Note: math.pi for adjustment x axis as x * pi
    ax.plot(x, y, z, color='gray', ls="-", linewidth=1)
    # Draw additional lines
    inter = abs(x_max - x_min) / num_additional_lines
    for i in range(num_additional_lines):
        xx = i * inter
        yy = np.sin((k * xx - omega * f) * np.pi)  # Note: math.pi for adjustment x axis as x * pi
        zz = np.cos((k * xx - omega * f) * np.pi)
        line = art3d.Line3D([xx, xx], [0, yy], [0, zz], color='gray', ls="--", linewidth=1)
        ax.add_line(line)
    # Draw spiral
    y = np.sin((k * x - omega * f) * np.pi)  # Note: math.pi for adjustment x axis as x * pi
    z = np.cos((k * x - omega * f) * np.pi)
    ax.plot(x, y, z)


# Global variables
x_min = 0.
x_max = 10.
y_min = -2.
y_max = 2.
z_min = -2.
z_max = 2.

num_additional_lines = 100

# Parameter of sine wave
k = 1.
omega = 0.1

# Generate arrange
x = np.arange(x_min, x_max, 0.005)

# Generate tkinter
root = tkinter.Tk()
root.title("Spiral")

# Generate figure and axes
fig = Figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect((2, 1, 1))

# Embed a figure in canvas
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(expand=True, fill='both')

# Animation
anim = animation.FuncAnimation(fig, update, interval=50, save_count=100)

# Toolbar
toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()
# Label and spinbox for k
label_k = tkinter.Label(root, text="k")
label_k.pack(side='left')
var_k = tkinter.IntVar(root)  # variable for spinbox-value
var_k.set(k)  # Initial value
s_k = tkinter.Spinbox(root, textvariable=var_k, from_=0, to=32, increment=1, command=lambda: change_k(var_k.get()), width=4)
s_k.pack(side='left')
# Label and spinbox for omega
label_o = tkinter.Label(root, text="omega")
label_o.pack(side='left')
var_o = tkinter.StringVar(root)  # variable for spinbox-value
var_o.set(omega)  # Initial value
s_o = tkinter.Spinbox(root, textvariable=var_o, format="%.2f", from_=-0.5, to=0.5, increment=0.01, command=lambda: change_o(var_o.get()), width=4)
s_o.pack(side='left')

# main loop
set_axis()
tkinter.mainloop()
