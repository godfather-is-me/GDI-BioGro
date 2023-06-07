# BioGro Hackathon - Good Data Institute

The Good Data Institute (GDI) Batch 4 Hackathon partnered with BioGro to solve the following problem - How do we create and enhance the value of the organic industry to benefit all stakeholders including BioGro. BioGro's role in the sector currently focuses on certification of organic products and our goal is to help their company using data driven insights to build the current market and increase value where it matters.

---

The app built in this repository is used as a tool that helps connect licensees with consumers as a high level marketplace. Customers that are intrested in organic products, especially those that trust and value the BioGro certification, can head to the website to lookup interested products and services available by BioGro. This by-flow-and-effect boosts BioGro's brand reputation and boosts visibility to all its certificate holders increasing the value of the certification.

## How to Use

#### Installation

The given app is run via `streamlit`. To reproduce the code, create a virtual environment and navigate into the folders of the files named below to run the following commands -

`pip install -r requirements.txt`

`streamlit run app.py`

---

#### Repository Structure

The repository has the following files

```
data
├── BioGroClean.csv 
├── BioGroProds.csv 
├── inputs.csv
├── products.csv
└── stores.csv

map
├── app.py
├── customer.py
├── producer.py
├── data.py
└── testing.ipynb

scrapers
├── product_scraper.py
└── scraper.py
```

- The data folder has scraped and cleaned data required for the tool to run. inputs, products, and stores are the files that contain scraped input data, product data, and a user defined database of available stores respectively.
- The notebooks folder contains testing scripts to ensure the app is working and relevant inputs and outputs are working in sync. Notebooks are view-only and not required to run.
- The scraper folder contains py scripts that have scraped data from BioGro's website tool

---

#### Bugs

- There still exists a minor bug - when first selecting a store an "equal key length error" comes about but is fixed when a store is selected. After this it does not appear in the program.