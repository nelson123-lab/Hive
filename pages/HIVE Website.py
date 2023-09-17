import streamlit as st
import webbrowser

st.write("Hive is a user-friendly platform that connects individuals who want to make a difference in their community. With Hive, users can easily post and browse various types of donations, ranging from clothing and household items to food and electronics.")

st.write("Our app leverages location-based technology to connect users with nearby donation opportunities, making it convenient for both donors and recipients to connect and exchange items. Whether you're looking to declutter your home or in need of essential items, Hive provides a seamless and intuitive experience to facilitate the donation process.")

st.write("By fostering a sense of community and promoting sustainable practices, Hive empowers users to give back and make a positive impact on the lives of others. Join Hive today and be a part of the movement to create a more connected and compassionate world.")
if st.button('About Us'):
    webbrowser.open_new("https://snippetsofakshay.github.io/HIVE.github.io/")
