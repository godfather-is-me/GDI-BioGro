# BioGro Hackathon - Good Data Institute

The Good Data Institute Batch 4 Hackathon partnered with BioGro has given us the problem of creation and enhancement of value in the organic industry. BioGro's business model currently focuses on certification of organic products and our goal is to help their company using data driven insights to build the current market and increase revenue and value for all stakeholders involved.

---

The app built in this repository is used as a tool that helps connect producers with customers as a high level marketplace. Customer that are intrested in organic products, especially those that trust and value the BioGro certification, can head to the website to lookup interested products and services available by BioGro. This by-flow-and-effect boosts BioGro's brand reputation and creates exposure to all its certificate holders increasing the value of the certification.

### How to Use

---

#### Installation

The given app is run via `streamlit`. To reproduce the code, create a virtual environment and navigate into the folders of the files named below to run the following commands -

`pip install -r requirements.txt`
`streamlit run app.py`

#### Repository Structure

The repository has the following files

```
data
├── BioGroClean.csv 
├── BioGroProds.csv 
├── inputs.csv
├── products.csv
└── stores.csv

notebooks
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
- The notebooks folder contains testing scripts to ensure the app is working and relevant inputs and outputs are working in sync.
- The scraper folder contains py scripts that have scraped data from BioGro's website tool