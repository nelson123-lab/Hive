import streamlit as st

user_input = st.text_area("Enter your message", value="", height=100)
send_button = st.button("Send")

def generate_response(user_input):
    return "fuck you"
if send_button:
    # Process the user's message here
    # You can add your logic to handle the message and generate a response
    response = generate_response(user_input)
    st.text(response)
