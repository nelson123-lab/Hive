import streamlit as st
from pymongo import MongoClient
from PIL import Image
import io
from streamlit_extras.switch_page_button import switch_page

uri ="mongodb+srv://hasnainbharmal4:samu@donate.f4lgt98.mongodb.net/?retryWrites=true&w=majority"
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

def main():
    # Set the page layout to center the buttons
    with open('style.css') as f:
            st.markdown('<style>(f.read())</style>', unsafe_allow_html=True)

    # Add the donate button
    if st.button("Donate an Item", key="donate_button"):
        # Add your donate button logic here
        switch_page("Donate an item")

    # Add some space between the buttons
    st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)

    # Add the receive button
    if st.button("Receive an Item", key="receive_button"):
        # Add your receive button logic here
        switch_page("Search an item")

    # Close the container div
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()


# for data in donors_within_distance:
#     st.write("Donor Details:")
#     donor_info = donor_template(data)
#     st.markdown(donor_info)
    
#     st.write("Donor Images:")
#     for photo_data in data["photos"]:
#         st.image(Image.open(io.BytesIO(photo_data)), use_column_width=True)
    
#     st.write("-" * 50)  # Add a separator line between entries
