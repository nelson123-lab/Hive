import streamlit as st

# Title
st.title("Donate an Item")

# Create a form to collect user inputs
name = st.text_input("Name")
item = st.text_input("Item Name")
count = st.number_input("Count", min_value=1, step=1)
category = st.selectbox("Category", ["Electronics", "Clothing", "Food", "Other"])
photos = st.file_uploader("Upload Photos", accept_multiple_files=True)
location = st.text_input("Location")

# Submit button
if st.button("Submit"):
    st.success("Form Submitted Successfully!")
    st.write("Name:", name)
    st.write("Item:", item)
    st.write("Count:", count)
    st.write("Category:", category)
    st.write("Location:", location)
    
    # Display uploaded photos
    if photos:
        st.write("Photos:")
        for photo in photos:
            st.image(photo, caption=f"Uploaded by {name}", use_column_width=True)