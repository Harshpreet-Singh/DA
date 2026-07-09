import pandas as pd

df = pd.read_csv('data/sas_combine.csv')
# print(df)

# rename the column names --
# df.rename(columns={'Unnamed: 0': 'Index', 'Unnamed: 1': 'Name', 'Unnamed: 2': 'Age'}, inplace=True)
# rename _2Ks63 
# df.rename(columns={'_2Ks63': 'Price'}, inplace=True)
# print(df)

# print(df.head())
# print('\n\n\n')
# print(df.tail())
# print('\n\n\ndataframe shape:')

# print(df.shape)
# print('\n\n\n')

# print(df.columns)
# print('\n\n\n')

# print(df.info())
# print('\n\n\n')

# print(df.describe(include="all"))
# print('\n\n\n')

# print(df.sample(5))

df.rename(columns={
    "_2Ks63":"price",
    "YBbhy":"property_details",
    "_2poNJ":"title",
    "_2VQu4":"location",
    "_2jcGx":"posted",
    "_1DNjI href":"url"
}, inplace=True)


# print(df.isnull().sum())

# lets remove the url column as it is not needed for our analysis
df.drop(columns=['url'], inplace=True)

# print(df.head())
# print(df[df['property_details'].isnull()].head(10))
# print(df['property_details'].dropna().head(10))

# SPLIT THE PROPERTY DETAILS COLUMN INTO 3 COLUMNS
df[['bhk', 'bathroom', 'area']] = df['property_details'].str.split(' - ', expand=True)
# print(df[['bhk', 'bedroom', 'area']].head())

df.drop(columns=['property_details'], inplace=True)
df.drop(columns=['posted'], inplace=True)



df["price"] = (
    df["price"]
      .str.replace("₹", "", regex=False)
      .str.replace(",", "", regex=False)
      .str.strip()
)
df['price'] = df['price'].astype("Int64")

# print(df['price'].head())
# print(df["price"].dtype)
# print(df.info())
# print(df.head())

# ---------------------PRICE IS CLEANED UPTO HERE---------------------
# NOW IT'S TURN OF BHK COLUMN
# print(df["bhk"].value_counts(dropna=False))

# Step 1: Replace 4+ BHK
df["bhk"] = df["bhk"].str.replace("4+ BHK", "4 BHK", regex=False)

# Step 2: Remove " BHK"
df["bhk"] = df["bhk"].str.replace(" BHK", "", regex=False)

# Step 3: Convert to a numeric type
df["bhk"] = df["bhk"].astype("Int64")

# print(df.head())


# NOW IT'S TURN OF BEDROOM COLUMN
# print(df["bathroom"].value_counts(dropna=False))
# this also contain NaN and 4+ so repeat the same steps as bhk column
# Step 1: Replace 4+ BHK
df["bathroom"] = df["bathroom"].str.replace("4+ Bathroom", "4 Bathroom", regex=False)

# Step 2: Remove " bathroom"
df["bathroom"] = df["bathroom"].str.replace(" Bathroom", "", regex=False)

# Step 3: Convert to a numeric type
df["bathroom"] = df["bathroom"].astype("Int64")

# bathroom count is specified in bhk column so we can drop the bathroom column
# df.drop(columns=['bathroom'], inplace=True)

# print(df.head())

# NOW IT'S TURN OF AREA COLUMN
# print(df['area'].value_counts(dropna=False))

# no NaN or x+ value case here so just replace " sqft" and convert to numeric type
df['area'] = df['area'].str.replace(" sqft", "", regex=False)

df["area"] = df['area'].astype("Int64")






# NOW COMES DROPPING NaN BHK VALUE ROWS 
df.dropna(subset=['bhk'], inplace=True)



# get the count of duplicate rows in the dataframe
# print(df.duplicated().sum() )

# drop the duplicate rows in the dataframe =
df.drop_duplicates(inplace=True)



# print(df.head())

# print(df.info())
# print(df.describe())


# FOLLOWING ARE SOME OF THE EXAMPLES OF HOW TO FILTER THE DATAFRAME BASED ON CERTAIN CONDITIOINS
# print(df.value_counts([df["area"] == 0]))
# print(df.value_counts([df["area"] > 10000]))
# print(df[df["price"] > 100000][["title", "price"]])
# print(df[df["area"] > 10000])


# LETS REMOVE THE ROWS WHERE TITLE HAS 'SALE' IN IT
# df = df[~df['title'].str.contains('sale', case = False, na = False)]
df = df[(df["area"] > 0) & (df["area"] <= 10000)]

sale_keywords = "sale|sell|ready to move|cr|crore|lakh"
df = df[~df["title"].str.contains(sale_keywords, case=False, na=False)]
df = df[df["price"] < 100000]   # Remove prices >= ₹1 lakh
print(df[df["price"] > 100000][["title", "price"]])  # no output now


print(df)