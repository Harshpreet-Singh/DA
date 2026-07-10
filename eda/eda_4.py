# Bivariate Analysis(relationship between two columns).
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sas_combine.csv')

df.rename(columns={
    "_2Ks63":"price",
    "YBbhy":"property_details",
    "_2poNJ":"title",
    "_2VQu4":"location",
    "_2jcGx":"posted",
    "_1DNjI href":"url"
}, inplace=True)

df.drop(columns=['url'], inplace=True)

df[['bhk', 'bathroom', 'area']] = df['property_details'].str.split(' - ', expand=True)
df.drop(columns=['property_details'], inplace=True)
df.drop(columns=['posted'], inplace=True)

df["price"] = (
    df["price"]
      .str.replace("₹", "", regex=False)
      .str.replace(",", "", regex=False)
      .str.strip()
)

df['price'] = df['price'].astype("Int64")
df["bhk"] = df["bhk"].str.replace("4+ BHK", "4 BHK", regex=False)
df["bhk"] = df["bhk"].str.replace(" BHK", "", regex=False)
df["bhk"] = df["bhk"].astype("Int64")

df["bathroom"] = df["bathroom"].str.replace("4+ Bathroom", "4 Bathroom", regex=False)
df["bathroom"] = df["bathroom"].str.replace(" Bathroom", "", regex=False)
df["bathroom"] = df["bathroom"].astype("Int64")

df['area'] = df['area'].str.replace(" sqft", "", regex=False)
df["area"] = df['area'].astype("Int64")

df.dropna(subset=['bhk'], inplace=True)
df.drop_duplicates(inplace=True)

df = df[(df["area"] > 0) & (df["area"] <= 10000)]
sale_keywords = "sale|sell|ready to move|cr|crore|lakh"
df = df[~df["title"].str.contains(sale_keywords, case=False, na=False)]
df = df[df["price"] < 100000]   # Remove prices >= ₹1 lakh

# DATA CLEANING DONE UPTO HERE

# ========================================================================================================================================

# EDA PROCESS BELOW ->

# Method 1: Pivot Table (First)
# This lets you inspect the values before plotting.
# pivot = pd.pivot_table(
#     df,
#     values="price",
#     index="location",
#     columns="bhk",
#     aggfunc="mean"
# )
# print(pivot.round(0))


# Method 2: Filter Locations with at least 10 Listings
# This prevents locations with just one expensive property from dominating the chart.
location_count = df["location"].value_counts()
valid_locations = location_count[location_count >= 10].index
filtered_df = df[df["location"].isin(valid_locations)]
pivot = pd.pivot_table(
    filtered_df,
    values="price",
    index="location",
    columns="bhk",
    aggfunc="mean"
)
print(pivot.round().astype("Int64"))


# Method 4: Plot Grouped Bar Chart  Price_vs_BHK_vs_Location

top_locations = df["location"].value_counts().head(10).index

top_df = df[df["location"].isin(top_locations)]

pivot = pd.pivot_table(
    top_df,
    values="price",
    index="location",
    columns="bhk",
    aggfunc="mean"
)

pivot.plot(
    kind="bar",
    figsize=(13,6),
    edgecolor="black"
)

plt.title("Average Monthly Rent by BHK (Top 10 Locations)")
plt.xlabel("Location")
plt.ylabel("Average Rent (₹)")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.legend(title="BHK")

plt.tight_layout()
plt.show()