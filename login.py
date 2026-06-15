import streamlit as st

def show_login():
    st.subheader("Login Section")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        st.success(f"Hi {username}, Login success!")
