import streamlit as st
from pymongo import MongoClient
import io 
from PIL import Image

# Title
st.title("Donate an Item")

uri = "mongodb+srv://hasnainbharmal4:samu@donate.f4lgt98.mongodb.net/?retryWrites=true&w=majority"
# Connect to MongoDB
client = MongoClient(uri)
db = client["Donate_app"]
users_collection = db["donations"]

# Create a form to collect user inputs
name = st.text_input("Name")
item = st.text_input("Item Name")
count = st.number_input("Count", min_value=1, step=1)
category = st.selectbox("Category", ["Electronics", "Clothing", "Food", "Other"])
photos = st.file_uploader("Upload Photos", accept_multiple_files=True)
location = st.text_input("Location")



if st.button("Submit"):

    photo_binary = []   
    # Display uploaded photos
    if photos:

        st.write("Photos:")
        for photo in photos:
            st.image(photo, caption=f"Uploaded by {name}", use_column_width=True)
            image = Image.open(photo)
            with io.bytesIO() as output:
                image.save(output, format = 'png')
                binary = output.getvalue()
            
            photo_binary.append(binary)
    
    user_data = {
        "Name:", name,
        "Item:", item,
        "Count:", count,
        "Category:", category,
        "Location:", location,
        "Image:",photo_binary,
        "Flag:", 1
    }
    users_collection.insert_one(user_data)

            
            