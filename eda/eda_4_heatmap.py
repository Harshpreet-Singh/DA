# ========================================================================================================================================
import pandas as pd
import matplotlib.pyplot as plt
# ========================================================================================================================================

df = pd.read_csv('./data/sas_cleaned_data.csv')

# EDA PROCESS BELOW ->

# Top 10 most common locations
top_locations = df["location"].value_counts().head(10).index
top_df = df[df["location"].isin(top_locations)]

# Create pivot table
pivot = pd.pivot_table(
    top_df,
    values="price",
    index="location",
    columns="bhk",
    aggfunc="mean"
)

print(pivot.round())

# Convert to float NumPy array (BEST FIX)
heatmap_data = pivot.to_numpy(dtype=float, na_value=float("nan"))

plt.figure(figsize=(8, 6))

plt.imshow(heatmap_data, aspect="auto", cmap="viridis")

plt.colorbar(label="Average Rent (₹)")

plt.xticks(range(len(pivot.columns)), pivot.columns)
plt.yticks(range(len(pivot.index)), pivot.index)

# Write average rent inside each cell
for i in range(len(pivot.index)):
    for j in range(len(pivot.columns)):
        value = heatmap_data[i, j]

        if not pd.isna(value):
            plt.text(
                j,
                i,
                f"{value:.0f}",
                ha="center",
                va="center",
                fontsize=9,
                color="white"
            )

plt.title("Average Monthly Rent by BHK Across Top 10 Locations")
plt.xlabel("BHK")
plt.ylabel("Location")

plt.tight_layout()
plt.show()