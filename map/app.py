import streamlit as st
import data as dt

import producer as pd
import customer as ct


def draw_sidebar():
    topics = [
        "Welcome",
        "Producer's view",
        "Customer's view"
    ]

    st.sidebar.title("Contents")
    page = st.sidebar.radio("Radio", topics, label_visibility="collapsed")

    if page == topics[0]:
        pass
    elif page == topics[1]:
        pd.draw_all()
    elif page == topics[2]:
        pass

def draw_main():
    draw_sidebar()

draw_main()