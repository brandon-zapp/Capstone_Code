import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

num_points = 50
lats = np.linspace(37.7749, 34.0522, num_points)
lons = np.linspace(-122.4194, -118.2437, num_points)
alts = np.sin(np.linspace(0, np.pi, num_points)) * 10000

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

(line,) = ax.plot([], [], [], color="red", lw=2)
(point,) = ax.plot([], [], [], marker="o", color="blue", ms=6)

ax.set_xlim(min(lons), max(lons))
ax.set_ylim(min(lats), max(lats))
ax.set_zlim(0, max(alts))


def update(frame):
    line.set_data(lons[:frame], lats[:frame])
    line.set_3d_properties(alts[:frame])

    point.set_data([lons[frame - 1]], [lats[frame - 1]])
    point.set_3d_properties([alts[frame - 1]])
    return line, point


ani = animation.FuncAnimation(
    fig, update, frames=num_points, interval=50, blit=False
)
ani.save("flight_path.gif", writer="pillow")
plt.show()