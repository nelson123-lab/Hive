import streamlit as st
from pymongo import MongoClient
from PIL import Image
import io

# Connect to MongoDB (replace with your MongoDB connection details)
client = MongoClient("mongodb://your_username:your_password@your_mongodb_host:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

# Title
st.title("Item Search")

# Create a search bar
search_query = st.text_input("Enter an item to search for")

# Perform the search
if search_query:
    results = collection.find({"$text": {"$search": search_query}})
    
    # Display search results
    st.subheader("Search Results:")
    
    for result in results:
        st.write("Name:", result["name"])
        st.write("Item:", result["item"])
        st.write("Location:", result["location"])
        st.write("Contact:", result["contact"])
        
        # Display the image
        st.image(Image.open(io.BytesIO(result["photo"])), use_column_width=True)
        
        st.write("-" * 50)  # Add a separator line between entries
