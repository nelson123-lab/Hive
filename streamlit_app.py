import streamlit as st
import bcrypt
from pymongo import MongoClient


st.set_page_config(page_title="Hive", page_icon="#",)
st.image('HIVE.jpg', use_column_width=True)
st.title("Welcome to Hive")
st.sidebar.success("Select a page")

uri = "mongodb+srv://hasnainbharmal4:samu@donate.f4lgt98.mongodb.net/?retryWrites=true&w=majority"
# Connect to MongoDB
client = MongoClient(uri)
db = client["Donate_app"]
users_collection = db["users"]

# Login form
def login():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Retrieve user details from the database
        user = users_collection.find_one({"username": username})

        if user:
            # Verify the password
            if bcrypt.checkpw(password.encode('utf-8'), user['password']):
                st.success("Logged in as {}".format(username))
                # Redirect to the desired page
            else:
                st.error("Invalid username or password")
        else:
            st.error("Invalid username or password")

# Sign-up form
def signup():
    st.header("Sign Up")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert user details into the database
        user_data = {
            "username": username,
            "email": email,
            "password": hashed_password
        }
        users_collection.insert_one(user_data)
        st.success("Successfully registered!")

# Run the Streamlit app
def main():
    # Display the login or sign-up form based on user selection
    form_choice = st.selectbox("Select an option:", ("Login", "Sign Up"))

    if form_choice == "Login":
        login()
    elif form_choice == "Sign Up":
        signup()

if __name__ == '__main__':
    main()
