import streamlit as st
from pymongo import MongoClient
from PIL import Image
import io

uri = "mongodb+srv://admin:admin@donate.f4lgt98.mongodb.net/?retryWrites=true&w=majority"
# Connect to MongoDB
client = MongoClient(uri)
db = client["Donate_app"]
users_collection = db["donations"]

# Define a function to create a donor template
def donor_template(data):
    template = """
    *Name:* {}
    *Item:* {}
    *Distance from Current Location:* {} km
    *Contact:* {}
    """.format(data["name"], data["item"], data["location"], data["contact"])
    
    return template

# Title and distance filter
st.title("Donors Gallery")
max_distance = st.slider("Maximum Distance (in km)", min_value=0, max_value=100, value=10)

# Display donors within the specified distance from the current location
donors_within_distance = users_collection.find({"location": {"$lte": max_distance}}, {"_id": 0, "name": 1, "item": 1, "location": 1, "contact": 1, "photos": 1})

for data in donors_within_distance:
    st.write("Donor Details:")
    donor_info = donor_template(data)
    st.markdown(donor_info)
    
    st.write("Donor Images:")
    for photo_data in data["photos"]:
        st.image(Image.open(io.BytesIO(photo_data)), use_column_width=True)
    
    st.write("-" * 50)  # Add a separator line between entries