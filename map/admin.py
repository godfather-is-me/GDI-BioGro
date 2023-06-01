import streamlit as st
import datetime

import data as dt

def title():
    """
    Title with header and informattion
    """
    st.markdown("# Admin \n---")
    st.markdown("#### New store details")

def store_input():
    """
    Function to get store data from the user and input into the database
    """
    with st.form("store_form"):
        name = st.text_input("Store Name")
        addy = st.text_input("Store Address")                       # Use Google Maps API to get lat long

        st.markdown("---")

        lat = st.number_input("Store latitude (if known)")
        lon = st.number_input("Store longtitude (if known)")

        st.markdown("---")

        # Accessibility
        open_time = st.time_input("Opening time", datetime.time(8, 30))
        close_time = st.time_input("Closing time", datetime.time(18, 30))
        wheel_access = st.checkbox("Wheelchair accessible?")
        pets_allowed = st.checkbox("Pets allowed?")


        #slider_val = st.slider("Form slider")
        #checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(name, addy, lat, lon, open_time, close_time, wheel_access, pets_allowed)

def draw_all():
    title()
    store_input()