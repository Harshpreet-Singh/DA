# ========================================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
# ========================================================================================================================================

df = pd.read_csv('./data/sas_cleaned_data.csv')

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

# print(df["bathroom"].value_counts())

# plt.figure(figsize=(7,5))
# df["bathroom"].value_counts().sort_index().plot(
#     kind="bar",
#     edgecolor="black"
# )
# plt.title("Distribution of Bathrooms")
# plt.xlabel("Number of Bathrooms")
# plt.ylabel("Number of Properties")
# plt.grid(axis="y", linestyle="--", alpha=0.5)

# plt.show()
