import pydeck as pdk

# Coordinate format: [longitude, latitude, altitude_meters, timestamp_seconds]
flight_coordinates = [
    [-122.4194, 37.7749, 100, 0],
    [-120.0000, 36.0000, 5000, 100],
    [-118.2437, 34.0522, 200, 200],
]

# Create an animated flight path layer
trips_layer = pdk.Layer(
    "TripsLayer",
    data=[{"path": flight_coordinates}],
    get_path="path",
    get_timestamps="path.map(p => p[3])",
    get_color=[255, 100, 0],  # Bright orange trail
    width_min_pixels=4,
    trail_length=50,  # Tail length behind the moving plane
    current_time=100,
)

# Position camera above California angled down
view_state = pdk.ViewState(
    latitude=36.0,
    longitude=-120.0,
    zoom=6,
    pitch=50,  # 3D tilt angle
    bearing=0,
)

# Uses built-in dark map tiles automatically
deck = pdk.Deck(
    layers=[trips_layer],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/dark-v10",  # or "light", "satellite"
)

deck.to_html("flight_on_map.html")