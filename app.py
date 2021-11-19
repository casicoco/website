import streamlit as st
'''
# My amazing website made with :love
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know apickupthing about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

import datetime

d = st.date_input("pickup date", datetime.date(2019, 7, 6))
t = st.time_input("pickup time", datetime.time(8,45))
st.write('Pickup:', d, t)


from streamlit_folium import folium_static
import folium
import os
import pandas as pd

m = folium.Map(location=[40.7128, 286], zoom_start=11)

pickup = {
    'lat': 40.7128,  #.7128,#° N,
    'lon': 286,  #74.0060} #° W
    'city': 'New York'
}

folium.Marker(
    location=[pickup['lat'], pickup['lon']],
    popup=pickup['city'],
    icon=folium.Icon(color="red", icon="car"),
).add_to(m)

drop = {
    'lat': 40.7128,  #.7128,#° N,
    'lon': 286,  #74.0060} #° W
    'city': 'New York'
}

folium.Marker(
    location=[drop['lat'], drop['lon']],
    popup=drop['city'],
    icon=folium.Icon(color="red", icon="car"),
).add_to(m)


from folium.plugins import MousePosition

MousePosition().add_to(m)
formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
folium.LatLngPopup().add_to(m)

MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Coordinates:",
    lat_formatter=formatter,
    lng_formatter=formatter,
).add_to(m)


def color_function(feat):
    return "red" if int(feat["properties"]["code"][:1]) < 5 else "blue"


# folium.GeoJson(
#     geojson_path,
#     name="geojson",
#     style_function=lambda feat: {
#         "weight": 1,
#         "color": "black",
#         "opacity": 0.25,
#         "fillColor": color_function(feat),
#         "fillOpacity": 0.25,
#     },
#     highlight_function=lambda feat: {
#         "fillColor": color_function(feat),
#         "fillOpacity": .5,
#     },
#     tooltip=folium.GeoJsonTooltip(fields=['code', 'nom'],
#                                   aliases=['Code', 'Name'],
#                                   localize=True),
# ).add_to(m)

folium_static(m)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
