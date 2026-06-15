import streamlit as st
import login
import booking
import view_bookings # Import pannunga

st.sidebar.title("Navigation")
# Menu-la "View Bookings"-ai add pannunga
menu = ["Home", "Login", "Book Tickets", "View Bookings"] 
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.title("Travel Booking App ✈️")
    st.write("Welcome to your travel dashboard!")

elif choice == "Login":
    login.show_login()

elif choice == "Book Tickets":
    booking.show_booking()

elif choice == "View Bookings":
    view_bookings.show_view() # Function-ai call pannunga
