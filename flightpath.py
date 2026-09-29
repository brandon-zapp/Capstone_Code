import numpy as np
import plotly.graph_objects as go

# Sample flight coordinate data: (Latitude, Longitude, Altitude in meters)
num_points = 100
lats = np.linspace(37.7749, 34.0522, num_points)  # SF to LA
lons = np.linspace(-122.4194, -118.2437, num_points)
alts = np.sin(np.linspace(0, np.pi, num_points)) * 10000  # Parabolic altitude profile

# Create 3D Scatter plot
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=lons,
            y=lats,
            z=alts,
            mode="lines+markers",
            line=dict(color="red", width=4),
            marker=dict(size=3, color="blue"),
        )
    ]
)

fig.update_layout(
    title="3D Flight Path",
    scene=dict(
        xaxis_title="Longitude",
        yaxis_title="Latitude",
        zaxis_title="Altitude (m)",
    ),
)

fig.show()