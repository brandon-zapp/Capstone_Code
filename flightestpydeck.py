import pydeck as pdk

# Sample path: [longitude, latitude, timestamp_in_seconds]
flight_path = [
    [-122.4194, 37.7749, 0],
    [-120.0000, 36.0000, 100],
    [-118.2437, 34.0522, 200],
]

layer = pdk.Layer(
    "TripsLayer",
    data=[{"path": flight_path}],
    get_path="path",
    get_timestamps="path.map(p => p[2])",
    get_color=[255, 0, 128],
    opacity=0.8,
    width_min_pixels=5,
    trail_length=30,  # Length of the visible trail behind the moving point
    current_time=100,  # Update this value to move the animation forward
)

view_state = pdk.ViewState(
    latitude=36.0, longitude=-120.0, zoom=6, pitch=45
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html("flight_animation.html")