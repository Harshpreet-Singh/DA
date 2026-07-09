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

print(df.shape)  # (5106, 6)
print(df.columns) # Index(['price', 'title', 'location', 'bhk', 'bathroom', 'area'], dtype='str')
print(df.info())
"""
<class 'pandas.DataFrame'>
Index: 5106 entries, 0 to 5621
Data columns (total 6 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   price     5106 non-null   Int64
 1   title     5106 non-null   str  
 2   location  5106 non-null   str  
 3   bhk       5106 non-null   Int64
 4   bathroom  5106 non-null   Int64
 5   area      5106 non-null   Int64
dtypes: Int64(4), str(2)
memory usage: 299.2 KB
None
"""


print(df.describe())