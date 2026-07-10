# ========================================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# ========================================================================================================================================
df = pd.read_csv('./data/sas_cleaned_data.csv')
# EDA PROCESS BELOW ->
# import seaborn as sns

# plt.figure(figsize=(9,6))
# top_locations = df["location"].value_counts().head(10).index

# top_df = df[df["location"].isin(top_locations)]


# pivot = pd.pivot_table(
#     top_df,
#     values="price",
#     index="location",
#     columns="bhk",
#     aggfunc="mean"
# )

# pivot = pivot.astype(float)

# plt.figure(figsize=(10,6))

# sns.heatmap(
#     pivot,
#     annot=True,
#     fmt=".0f",
#     cmap="YlOrRd",
#     linewidths=0.5
# )

# plt.title("Average Monthly Rent by BHK Across Top 10 Locations")
# plt.xlabel("BHK")
# plt.ylabel("Location")
# plt.subplots_adjust(left=0.35)
# plt.show()


corr = df[["price", "area", "bhk", "bathroom"]].corr()

corr = df[["price", "area", "bhk", "bathroom"]].corr()

plt.figure(figsize=(6, 5))

ax = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

# Move column names (price, area, ...) to the top
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')

# Keep row names on the left
plt.yticks(rotation=0)
plt.xticks(rotation=0)

plt.title("Correlation Heatmap", pad=20)

plt.show()