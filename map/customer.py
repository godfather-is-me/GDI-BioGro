import streamlit as st
import data as dt

def title():
    """
    Titles and information
    """
    st.markdown("# Customer")

def map_output():
    st.map(dt.get_stores(), zoom=5)

def select_option():
    st.markdown("---")
    st.markdown("#### What Organic products would you like to purchase today?")

    option = st.selectbox(
        "Product Name",
        dt.get_products()
    )

def draw_all():
    title()
    map_output()
    select_option()