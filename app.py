import streamlit as st
import login

st.sidebar.title("Navigation")
menu = ["Home", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.title("Travel Booking App ✈️")
    st.write("Welcome to your travel dashboard!")

elif choice == "Login":
    login.show_login()
