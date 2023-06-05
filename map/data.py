import streamlit as st
import pandas as pd

# Global df
df = pd.read_csv("../data/products.csv")
sr = pd.read_csv("../data/stores.csv")

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
    return df[df["Licensee"] == name]

def get_products():
    """
    Function to get all products from the list
    """
    return df["Product"].unique()

def get_all_products():
    """
    Function to get the products dataframe
    """
    return df

def get_stores():
    """
    Get store information
    """
    return sr

def get_store_names():
    """
    Get store names only
    """
    return sr["Name"]

def get_filtered_store_names(product_name: str):
    """
    Returns a list of filtered stores based on product requirements
    and store availibility
    """
    products = df[df["Product"] == product_name]
    avail = products[products["Available"] == True]
    stores = set()
    for _, row in avail.iterrows():
        if not (type(row["Store #"]) == float and pd.isna(row["Store #"])):
            if type(row["Store #"]) == list:
                if not (row["Store #"] == []):
                    # Non null and not empty
                    for s in row["Store #"]:
                        stores.add(s)
            else:   # Not list - single value
                stores.add(row["Store #"])
                
    return stores

def get_filtered_stores(product_name: str):
    """
    Return store data based on filtered store names
    """
    names = get_filtered_store_names(product_name)
    return sr[sr["Name"].isin(names)]

def put_stores():
    """
    Function to put stores into data given values
    """
    pass