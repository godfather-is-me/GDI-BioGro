import streamlit as st
import data as dt

def title():
    """
    Titles and information
    """
    st.markdown("# Customer")

def select_option():
    st.markdown("---")
    st.markdown("#### What Organic products would you like to purchase today?")

    option = st.selectbox(
        "Product Name",
        dt.get_products()
    )
    return option

def map_output(product_name: str):
    st.map(dt.get_filtered_stores(product_name), zoom=5)
    # st.map(dt.get_stores(), zoom=5)

def store_details_output(product_name: str):
    """
    Borrow names from map output
    """
    for _, row in dt.get_filtered_stores(product_name).iterrows():
        st.markdown("---")
        st.write(f"### {row['Name']}")

        cols = st.columns(3)
        with cols[0]:
            st.write(row["Address"])
        with cols[1]:
            st.write("##### Timings")
            st.write(row["Open time"])
            st.write(row["Close time"])
        with cols[2]:
            st.write("##### Accessibility")
            st.write("Wheelchair Acessible:", row["Wheelchair Accessible"])
            st.write("Pets Allowed:", row["Pets Allowed"])

def robot_check():
    """
    Checkbox to check if you are a robot
    """
    val = st.checkbox("Are you a robot?")
    if val:
        #st.dark_theme()
        st.markdown("I believe you :)")
    return val

def draw_all():
    title()
    if robot_check():
        option = select_option()
        map_output(option)
        store_details_output(option)