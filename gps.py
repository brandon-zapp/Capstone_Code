"""
3D Balloon Flight Path Visualization
--------------------------------------
Plots a weather-balloon-style flight path (lat, lon, altitude) using
Plotly's Scatter3d, with points every 5 minutes.

Replace the `generate_sample_data()` function with your real data,
or load it from a CSV with columns: time, lat, lon, altitude
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta


def generate_sample_data(n_points=40, start_lat=39.7392, start_lon=-104.9903):
    """
    Generates fake balloon flight data:
    - Ascends steadily, bursts at peak altitude, then descends (parachute) faster.
    - Drifts horizontally with a bit of random wind wobble.
    """
    np.random.seed(42)

    burst_index = int(n_points * 0.6)  # balloon "bursts" 60% of the way through

    altitudes = []
    for i in range(n_points):
        if i <= burst_index:
            # ascent: roughly linear climb to ~30km with noise
            alt = (i / burst_index) * 30000 + np.random.normal(0, 200)
        else:
            # descent: faster drop (parachute) back to ground
            frac = (i - burst_index) / (n_points - burst_index)
            alt = 30000 * (1 - frac) ** 1.5 + np.random.normal(0, 150)
        altitudes.append(max(alt, 0))

    # simulate horizontal drift (wind pushing it generally eastward)
    lats = [start_lat]
    lons = [start_lon]
    for i in range(1, n_points):
        lats.append(lats[-1] + np.random.normal(0.003, 0.002))
        lons.append(lons[-1] + np.random.normal(0.01, 0.003))

    times = [datetime(2026, 9, 10, 8, 0) + timedelta(minutes=5 * i) for i in range(n_points)]

    return pd.DataFrame({
        "time": times,
        "lat": lats,
        "lon": lons,
        "altitude_m": altitudes
    })


def plot_flight_3d(df):
    fig = go.Figure(data=go.Scatter3d(
        x=df["lon"],
        y=df["lat"],
        z=df["altitude_m"],
        mode="lines+markers",
        line=dict(width=4, color="darkblue"),
        marker=dict(
            size=4,
            color=df["altitude_m"],
            colorscale="Turbo",
            colorbar=dict(title="Altitude (m)"),
        ),
        text=[f"{t:%H:%M}<br>Alt: {a:.0f} m" for t, a in zip(df["time"], df["altitude_m"])],
        hoverinfo="text"
    ))

    # mark launch and landing points
    fig.add_trace(go.Scatter3d(
        x=[df["lon"].iloc[0]], y=[df["lat"].iloc[0]], z=[df["altitude_m"].iloc[0]],
        mode="markers+text", marker=dict(size=6, color="green"),
        text=["Launch"], textposition="top center", showlegend=False
    ))
    fig.add_trace(go.Scatter3d(
        x=[df["lon"].iloc[-1]], y=[df["lat"].iloc[-1]], z=[df["altitude_m"].iloc[-1]],
        mode="markers+text", marker=dict(size=6, color="red"),
        text=["Landing"], textposition="top center", showlegend=False
    ))

    fig.update_layout(
        title="Sample 3D Balloon Flight Path (position every 5 minutes)",
        scene=dict(
            xaxis_title="Longitude",
            yaxis_title="Latitude",
            zaxis_title="Altitude (m)",
        ),
        margin=dict(l=0, r=0, t=40, b=0),
    )

    return fig


if __name__ == "__main__":
    df = generate_sample_data()
    fig = plot_flight_3d(df)
    fig.write_html("balloon_flight_3d.html")
    print("Saved plot to balloon_flight_3d.html")
    print(df.head())