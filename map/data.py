import streamlit as st
import pandas as pd

# Global df
df = pd.read_csv("../data/products.csv")

def get_licensees():
    """
    Function to get license holder names
        - For searchbox
    """
    return df["Licensee"].unique()

def get_prods_from_licensee(name: str):
    """
    Get products sold for a given license holder
    """
    return df[df["Licensee"] == name][["Product", "Variety", "Store #"]]