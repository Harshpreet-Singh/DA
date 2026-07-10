# ========================================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
# ========================================================================================================================================
df = pd.read_csv('./data/sas_cleaned_data.csv')
# EDA PROCESS BELOW ->

# avg_price = df.groupby("bhk")["price"].mean()
# print(avg_price)

# ploting graph of this reading

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


top_locations = df["location"].value_counts().head(10)

plt.figure(figsize=(10,6))

top_locations.plot(kind="bar", edgecolor="black")

plt.title("Top 10 Locations by Number of Listings")
plt.xlabel("Location")
plt.ylabel("Number of Listings")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
