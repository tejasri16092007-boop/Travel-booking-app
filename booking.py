import streamlit as st
import database

def show_booking():
    st.subheader("Book Your Tickets 🎫")
    source = st.text_input("Source Location")
    destination = st.text_input("Destination Location")
    travel_type = st.selectbox("Travel Type", ["Bus", "Train", "Flight"])
    date = st.date_input("Travel Date")
    
    if st.button("Book Now"):
        booking_details = {
            "source": source,
            "destination": destination,
            "type": travel_type,
            "date": str(date)
        }
        database.save_booking(booking_details)
        st.success("Ticket booked and saved successfully!")
