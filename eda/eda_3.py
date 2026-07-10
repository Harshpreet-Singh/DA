# Bivariate Analysis(relationship between two columns).
import pandas as pd
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

# avg_price = df.groupby("bhk")["price"].mean()
# print(avg_price)

# ploting graph of this reading
import matplotlib.pyplot as plt

# avg_price.plot(kind="bar", edgecolor="black")
# plt.title("Average Rent by BHK")
# plt.xlabel("BHK")
# plt.ylabel("Average Rent (₹)")
# plt.grid(axis="y", linestyle="--", alpha=0.5)
# plt.show()


# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# print(df.groupby("bhk")["area"].mean())

# scatter plot of price_vs_area
# plt.scatter(df["area"], df["price"])

# plt.xlabel("Area (sqft)")
# plt.ylabel("Price")
# plt.title("Price vs Area")
# plt.grid(axis="y", linestyle="--", alpha=0.5)
# plt.show()


# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# Top 10 Locations by Average Monthly Rent (Minimum 10 Listings)
# top10 = (
#     df.groupby("location")["price"]
#       .mean()
#       .sort_values(ascending=False)
#       .head(10)
# )
# plt.figure(figsize=(10,6))
# top10.plot(
#     kind="barh",
#     edgecolor="black"
# )
# plt.title("Top 10 Locations by Average Monthly Rent", fontsize=15)
# plt.xlabel("Average Rent (₹)")
# plt.ylabel("Location")
# plt.grid(axis="x", linestyle="--", alpha=0.5)
# plt.gca().invert_yaxis()   # Highest value on top
# plt.tight_layout()
# plt.show()


# top_locations = df["location"].value_counts().head(10)

# plt.figure(figsize=(10,6))

# top_locations.plot(kind="bar", edgecolor="black")

# plt.title("Top 10 Locations by Number of Listings")
# plt.xlabel("Location")
# plt.ylabel("Number of Listings")

# plt.xticks(rotation=45, ha="right")
# plt.grid(axis="y", linestyle="--", alpha=0.5)

# plt.tight_layout()
# plt.show()
