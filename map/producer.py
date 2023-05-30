import streamlit as st
import data as dt

from streamlit_searchbox import st_searchbox

def title():
    """
    Welcome title for producers
    """
    st.markdown("# Producer Page \n ---")

def select_options():
    option = st.selectbox(
        "Producer Name",
        dt.get_licensees()
    )

    st.markdown("---")
    st.markdown("### Product - Variety List")

    # Show vareity
    if not (option is None):
        for _, row in dt.get_prods_from_licensee(option).iterrows():
            st.markdown(f"##### Product: {row['Product']}\nVariety: {row['Variety']}\nStores: {row['Store #']} ---")

def draw_all():
    title()
    select_options()