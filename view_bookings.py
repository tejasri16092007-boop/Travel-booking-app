import streamlit as st
import json
import os

def show_view():
    st.subheader("Your Bookings 📋")
    file_path = "Data/bookings.json"
    
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
                if data:
                    st.table(data) # Idhu data-vai table format-la kaatum
                else:
                    st.write("No bookings yet!")
            except json.JSONDecodeError:
                st.write("No bookings found.")
    else:
        st.write("No bookings yet!")
