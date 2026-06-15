import streamlit as st
import login
import booking  # Indha line-ai marakkama add pannunga

st.sidebar.title("Navigation")
menu = ["Home", "Login", "Book Tickets"] # "Book Tickets"-ai menu-la add pannum
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.title("Travel Booking App ✈️")
    st.write("Welcome to your travel dashboard!")

elif choice == "Login":
    login.show_login()

elif choice == "Book Tickets":
    booking.show_booking() # Booking feature-ai load pannum
