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
    unique_key = 0
    if not (option is None):
        for _, row in dt.get_prods_from_licensee(option).iterrows():
            st.markdown("---")
            cols = st.columns(4)
            with cols[0]:
                checked = st.checkbox("Availability", value = row['Available'], key=unique_key)
                if checked:
                    select_stores()
            with cols[1]:
                st.markdown(f"Product : {row['Product']}")
            with cols[2]:
                st.markdown(f"Variety : {row['Variety']}")
            with cols[3]:
                if row['Store #'] is None:
                    st.markdown(f"Stores : None")
                else:
                    st.markdown(f"Stores : {row['Store #']}")
            unique_key += 1

def select_stores():
    pass

def draw_all():
    title()
    select_options()