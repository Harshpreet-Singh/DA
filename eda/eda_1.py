# ========================================================================================================================================
import pandas as pd
# ========================================================================================================================================

df = pd.read_csv('./data/sas_cleaned_data.csv')

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