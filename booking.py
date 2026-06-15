import streamlit as st

def show_booking():
    st.subheader("Book Your Tickets 🎫")
    
    # Booking inputs
    source = st.text_input("Source Location")
    destination = st.text_input("Destination Location")
    travel_type = st.selectbox("Travel Type", ["Bus", "Train", "Flight"])
    date = st.date_input("Travel Date")
    
    if st.button("Book Now"):
        st.success(f"Successfully booked your {travel_type} from {source} to {destination} on {date}!")
