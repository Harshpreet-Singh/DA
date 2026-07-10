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
* Relationship between area and bhk etc
* Relationship between 3 Things BHK, Location, Price
* Bathroom distribution
* Property listing trends

---

## Project Structure

```text
DA/
│   
├── data_cleaning.py
├── insights.md
├── readme.md
├── read_csv.py
├── read_csv_url.py
├── requirements.txt
│   
│   
├── data/
│       kharar_combine.csv
│       mohali_combine.csv
│       sas_cleaned_data.csv
│       sas_combine.csv
│ 
│ 
├── eda/
│   ├── eda_1.py
│   ├── eda_2.py
│   ├── eda_3.py
│   ├── eda_4.py
│   ├── eda_4_heatmap.py
│   └── eda_4_heatmap_seaborn.png
│
│
└── imgs/
    ├── Bivariate_Analysis/
    │   ├── eda_3_bhk_vs_price.png
    │   ├── eda_3_location_vs_count.png
    │   ├── eda_3_price_vs_area.png
    │   └── eda_3_top_10_location_vs_avg_rent.png
    │       
    │       
    ├── Multivariate_Analysis/
    │   ├── eda_4_heatmap_Correlation_Matrix.png
    │   ├── eda_4_heatmap_Price_vs_BHK_vs_Location(seaborn).png
    │   ├── eda_4_heatmap_Price_vs_BHK_vs_Location.png
    │   └── eda_4_Price_vs_BHK_vs_Location.png
    │       
    │       
    └── Univariate_Analysis/
        ├── eda_2_bathroom_bar_graph.png
        ├── eda_2_bhk_bar_graph.png
        ├── eda_2_price_box-plot.png
        └── eda_2_price_histogram.png
            
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
