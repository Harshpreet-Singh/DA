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


# DATA CLEANING DONE 
import matplotlib.pyplot as plt

# HISTOGRAM BELOW:
# plt.figure(figsize=(8,5))
# plt.hist(df["price"], bins=20)
# plt.title("Distribution of Rental Prices")
# plt.xlabel("Monthly Rent (₹)")
# plt.ylabel("Number of Properties")
# plt.show()

# FOLLOWING IS BETTER AND CLEANER HISTOGRAM
 
# plt.figure(figsize=(10,5))
# plt.hist(df["price"],
#          bins=25,
#          edgecolor="black")
# plt.title("Distribution of Monthly Rental Prices", fontsize=14)
# plt.xlabel("Monthly Rent (₹)", fontsize=12)
# plt.ylabel("Number of Properties", fontsize=12)
# plt.xticks(range(0, 100001, 10000), rotation=45)
# plt.grid(axis="y", linestyle="--", alpha=0.5)
# plt.tight_layout()
# plt.show()


# BOX PLOT BELOW: 
# plt.figure(figsize=(8,2))
# plt.boxplot(df["price"], vert=False)
# plt.title("Box Plot of Rental Prices")
# plt.show()



# print(df["bhk"].value_counts())

# print(df["bhk"].value_counts(normalize=True) * 100)

# HISTOGRAM OF BHK COLUMN BELOW
# plt.figure(figsize=(7,5))

# df["bhk"].value_counts().sort_index().plot(
#     kind="bar",
#     edgecolor="black"
# )

# plt.title("Distribution of BHK")
# plt.xlabel("BHK")
# plt.ylabel("Number of Properties")
# plt.grid(axis="y", linestyle="--", alpha=0.5)

# plt.show()




# HISTOGRAM OF bathroom COLUMN BELOW

print(df["bathroom"].value_counts())

plt.figure(figsize=(7,5))

df["bathroom"].value_counts().sort_index().plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Distribution of Bathrooms")
plt.xlabel("Number of Bathrooms")
plt.ylabel("Number of Properties")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()