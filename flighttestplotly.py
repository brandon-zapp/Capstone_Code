import numpy as np
import plotly.graph_objects as go

num_points = 50
lats = np.linspace(37.7749, 34.0522, num_points)
lons = np.linspace(-122.4194, -118.2437, num_points)
alts = np.sin(np.linspace(0, np.pi, num_points)) * 10000

# Base trace (empty or initial point)
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=[lons[0]],
            y=[lats[0]],
            z=[alts[0]],
            mode="lines+markers",
            line=dict(color="red", width=4),
            marker=dict(size=6, color="blue"),
        )
    ],
    layout=go.Layout(
        scene=dict(
            xaxis=dict(range=[min(lons), max(lons)]),
            yaxis=dict(range=[min(lats), max(lats)]),
            zaxis=dict(range=[0, max(alts) + 1000]),
            xaxis_title="Longitude",
            yaxis_title="Latitude",
            zaxis_title="Altitude (m)",
        ),
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    )
                ],
            )
        ],
    ),
    # Add frames to build the line point-by-point
    frames=[
        go.Frame(
            data=[
                go.Scatter3d(
                    x=lons[:k],
                    y=lats[:k],
                    z=alts[:k],
                    mode="lines+markers",
                    line=dict(color="red", width=4),
                    marker=dict(size=6, color="blue"),
                )
            ]
        )
        for k in range(1, num_points + 1)
    ],
)

fig.show()