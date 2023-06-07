import streamlit as st
import data as dt

import numpy as np
import pandas as pd

from streamlit_searchbox import st_searchbox

def title():
    """
    Welcome title for producers
    """
    st.markdown("# Licensee Page \n ---")

def select_options():
    option = st.selectbox(
        "Producer Name",
        dt.get_licensees(),
        index=1
    )

    st.markdown("---")
    st.markdown("### Product - Variety List")

    # Show vareity
    unique_key = 0
    if not (option is None):
        for _, row in dt.get_prods_from_licensee(option).iterrows():
            st.markdown("---")
            # Split into 4 columns
            cols = st.columns(4)
            with cols[0]:
                # Check box key
                key_str = "check_" + str(row["BioGro #"]) + '_' + str(unique_key)
                checked = st.checkbox("Availability", value = row['Available'], key=key_str)
            with cols[1]:
                st.markdown(f"Product : {row['Product']}")
            with cols[2]:
                st.markdown(f"Variety : {row['Variety']}")
            with cols[3]:
                if (type(row["Store #"]) == float and pd.isna(row["Store #"])) or row["Store #"] == []:
                    st.markdown(f"Stores : None")
                else:
                    st.markdown("Stores : ")
                    if type(row["Store #"]) == list:
                        for s in row['Store #']:
                            st.markdown(s)
                    else:
                        st.markdown(row["Store #"])

            # Next line searchbar
            if checked:
                selected = select_stores(row, key_str)
                dt.get_all_products().at[row["UID"], "Store #"] = selected

                if row["Available"] == False:
                    dt.get_all_products().at[row["UID"], "Available"] = True

            else:
                if row['Available'] == True:
                    dt.get_all_products().at[row["UID"], "Available"] = False
            unique_key += 1

def select_stores(row, key_str: str):
    """
    Function to select stores from a list of a searchbox
    """
    # Special key for multiselect
    key_str = "multi" + key_str[5:]

    if type(row["Store #"]) == float and pd.isna(row["Store #"]):
        selected = st.multiselect('Select Stores', dt.get_store_names(), key=key_str)
    else:
        selected = st.multiselect('Select Stores', dt.get_store_names(), row["Store #"], key=key_str)
    # st.write(selected)
    return selected

def draw_all():
    title()
    select_options()