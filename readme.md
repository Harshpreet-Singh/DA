# OLX Rental Property Data Analysis

A data analysis project that collects, cleans, and analyzes rental property listings scraped from **OLX** across **Mohali, Kharar, and SAS Nagar**. The project focuses on transforming raw scraped data into a clean, analysis-ready dataset and extracting meaningful insights through Exploratory Data Analysis (EDA).

---

## Project Objective

The objective of this project is to:

* Scrape rental property listings from OLX.
* Clean and preprocess raw data.
* Handle missing values, duplicates, and outliers.
* Prepare the dataset for analysis.
* Explore rental trends across different locations.
* Visualize important insights using Python.

---

## Datasets

The project contains separate datasets for:

* Mohali
* Kharar
* SAS Nagar

Each dataset follows the same cleaning and preprocessing pipeline.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib/Seaborn

---

## Data Cleaning Steps

The following preprocessing steps were performed:

* Renamed columns for better readability.
* Removed unnecessary columns.
* Split property details into separate columns:

  * BHK
  * Bathroom
  * Area
* Converted data types to numeric format.
* Handled missing values.
* Removed duplicate records.
* Filtered non-rental (sale) listings.
* Removed invalid and unrealistic values.
* Prepared the final dataset for analysis.

---

## Exploratory Data Analysis (EDA)

The project explores insights such as:

* Rental price distribution
* Most common BHK configuration
* Average rent by location
* Relationship between area and rent
* Bathroom distribution
* Property listing trends

---

## Project Structure

```text
OLX-Rental-Property-Analysis/
│
├── data/
│   ├── mohali.csv
│   ├── kharar.csv
│   └── sas_nagar.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── eda.ipynb
│
├── README.md
└── requirements.txt
```

---

## Future Improvements

* Merge all datasets into a single dataset.
* Build an interactive dashboard.
* Perform advanced statistical analysis.
* Create predictive models for rental price estimation.

---

## Author

**Harshpreet Singh**

Learning Data Analysis | Python | Pandas | SQL
