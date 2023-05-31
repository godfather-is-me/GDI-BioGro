import streamlit as st
from PIL import Image

def intro_image():
    """
    Output the BioGro logo
    """
    col1, col2, col3 = st.columns([1,2,1])
    image = Image.open("../data/BioGro-logo.jpg")

    with col1:
        st.write("")

    with col2:
        st.image(image, caption='BioGro')

    with col3:
        st.write("")
        

def title():
    """
    Welcome page title for the app demo
    """

    st.markdown("# Welcome \n ---")

def context():
    """
    Gives context about the app. (Information is taken from the readme file)
    """
    # Information
    pre_info = """The Good Data Institute Batch 4 Hackathon partnered with BioGro has given us the 
                problem of creation and enhancement of value in the organic industry. BioGro's business 
                model currently focuses on certification of organic products and our goal is to help their 
                company using data driven insights to build the current market and increase revenue and 
                value for all stakeholders involved."""
    post_info = """The app built in this repository is used as a tool that helps connect producers with customers 
                as a high level marketplace. Customer that are intrested in organic products, especially those 
                that trust and value the BioGro certification, can head to the website to lookup interested 
                products and services available by BioGro. This by-flow-and-effect boosts BioGro's brand 
                reputation and creates exposure to all its certificate holders increasing the value of the 
                certification."""
    
    # Outputs
    st.markdown(pre_info)
    st.markdown("---")
    st.markdown(post_info)

def draw_all():
    title()
    intro_image()
    context()
