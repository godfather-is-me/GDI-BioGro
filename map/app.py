import streamlit as st
import data as dt

import welcome as wc
import producer as pd
import customer as ct
import admin as ad


def draw_sidebar():
    topics = [
        "Welcome",
        "Producer's view",
        "Customer's view",
        "Admin's view"
    ]

    st.sidebar.title("Contents")
    page = st.sidebar.radio("Radio", topics, label_visibility="collapsed")

    if page == topics[0]:
        wc.draw_all()
    elif page == topics[1]:
        pd.draw_all()
    elif page == topics[2]:
        ct.draw_all()
    elif page == topics[3]:
        ad.draw_all()

def draw_main():
    draw_sidebar()

draw_main()