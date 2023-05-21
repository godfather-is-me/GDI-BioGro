import streamlit as st

def draw_sidebar():
    topics = [
        "Producer's view",
        "Customer's view"
    ]

    st.sidebar.title("Contents")
    page = st.sidebar.radio("Radio", topics, label_visibility="collapsed")

    if page == topics[0]:
        pass
    elif page == topics[1]:
        pass


def draw_main():
    draw_sidebar()

draw_main()