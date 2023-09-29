import streamlit as st
from pymongo import MongoClient
from PIL import Image
import io
import math
import geocoder
from dotenv import load_dotenv
import os


load_dotenv()

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Radius of the Earth in miles
    radius = 3959

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance

uri = os.getenv("API_KEY")
# Connect to MongoDB (replace with your MongoDB connection details)
client = MongoClient(uri)
db = client["Donate_app"]
users_collection = db["donations"]

# Title
st.title("Item Search")

# Get the user's location
g = geocoder.ip('me')
latitude, longitude = g.latlng[0], g.latlng[1]

# Display the location data
st.write(f"Detected Location = Latitude {latitude}, Longitude {longitude}")
# Create a search bar
search_query = st.text_input("Enter an item to search for")

max_distance = st.slider("Maximum Distance (in miles)", min_value=0, max_value=100, value=10)

# Display donors within the specified distance from the current location
donors_within_distance = users_collection.find({"location": {"$lte": max_distance}}, {"_id": 0, "name": 1, "item": 1, "location": 1, "contact": 1, "photos": 1})

# Create a filter button
apply_filter = st.button("Apply Filter")

# Perform the search when the filter button is clicked
if apply_filter:
    # Perform the search with the applied filter
    results = users_collection.find({"$text": {"$search": search_query}, "filter_field": "filter_value"})
else:
    # Perform the search without any filter
    results = users_collection.find({"$text": {"$search": search_query}})

# Display search results
st.subheader("Search Results:")
for result in results:
    # Display the result details
    st.write("Name:", result["name"])
    st.write("Item:", result["item"])
    st.write("Location:", result["location"])
    st.write("Contact:", result["contact"])
    st.image(Image.open(io.BytesIO(result["photo"])), use_column_width=True)
    st.write("-" * 50)  # Add a separator line between entries
