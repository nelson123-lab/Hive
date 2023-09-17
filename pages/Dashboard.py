import streamlit as st
from pymongo import MongoClient

uri = "mongodb+srv://admin:admin@donate.f4lgt98.mongodb.net/?retryWrites=true&w=majority"
# Connect to MongoDB
client = MongoClient(uri)
db = client["Donate_app"]
users_collection = db["donations"]

