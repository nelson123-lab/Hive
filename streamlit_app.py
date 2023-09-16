import streamlit as st
# import pymongo



# # Replace <connection_string> with your MongoDB connection string
# client = pymongo.MongoClient("<connection_string>")
# db = client["your_database_name"]
# user_collection = db.create_collection("users")

# Streamlit registration form
st.title("User Registration")
name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if password == confirm_password:
        user = {
            "name": name,                                                                            
            "email": email,
            "password": password
        }
        user_collection.insert_one(user)
        st.success("Registration successful!")
    else:
        st.error("Passwords do not match!")
# Streamlit login form

st.title("User Login")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = user_collection.find_one({"email": email})
    if user and user["password"] == password:
        st.success("Login successful!")
    else:
        st.error("Invalid credentials!")
