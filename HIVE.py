import streamlit as st
import bcrypt
from pathlib import Path
import json
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import _on_pages_changed, get_pages

DEFAULT_PAGE = "HIVE.py"
SECOND_PAGE_NAME = "Dashboard"


# all pages request
def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages

# clear all page but not login page
def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()

# show all pages
def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    # Replace all the missing pages
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()

# Hide default page
def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break

# calling only default(login) page  
clear_all_but_first_page()

st.image('HIVE.png', use_column_width=True)
st.title("Welcome to Hive")
# st.sidebar.success("Select a page")

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
                st.success("Logged In Sucessfully {}".format(username))
                # Redirect to the desired page
                show_all_pages()  # call all page
                hide_page(DEFAULT_PAGE.replace(".py", ""))  # hide first page
                switch_page(SECOND_PAGE_NAME)   # switch to second page
                # switch_page("Dashboard")
            else:
                st.error("Invalid username or password")
                clear_all_but_first_page()  # clear all page but show first page
        else:
            st.error("Invalid username or password")
            clear_all_but_first_page()  # clear all page but show first page

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
