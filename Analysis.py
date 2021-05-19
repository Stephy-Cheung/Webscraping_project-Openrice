import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Anaylsis on location
def filter_district(address):
    return address.split(",")[-1].strip()

df = pd.read_csv("openrice.csv")
df = df.drop_duplicates(["res_id"]).reset_index(drop=True)
df = df[df["review"] > 5] 

df["district"] = df["address"].apply(filter_district)

counts = df["district"].value_counts().rename("counts")
means = df.groupby("district")[["likes","dislikes","bookmarks","review"]].mean()
japan = means.join(counts)
japan["like_percetage"] = japan["likes"]/(japan["likes"] + japan["dislikes"])
japan["popularity"] = japan["like_percetage"]*japan["bookmarks"]
japan = japan.sort_values(by="popularity")
fig,ax = plt.subplots(figsize=(12,6))
ax.barh(japan.index, japan["popularity"],color="navy")
ax.set_xlabel('Popularity')
ax.set_ylabel('District')
plt.tight_layout()
plt.show()

# Analysis on price_range
df = pd.read_csv('openrice.csv')
df = df.drop_duplicates('res_id')
df['like_prop'] = df['likes'] / (df['likes'] + df['dislikes'])
df['popularity'] = df['bookmarks'] * df['like_prop']
mean_table = df[df['review']>5].groupby('price_range').mean()
corr_table = df[df['review']>5].corr()

fig, ax = plt.subplots(1, 1)
ax.bar(mean_table.iloc[[5,3,0,1,2,4],:].index, mean_table.iloc[[5,3,0,1,2,4],:]['popularity'],color=['navy'])
plt.ylabel('popularity')
plt.xlabel('price range')
plt.xticks(size=9)
plt.show()

# Analysis on cuisine
sns.set(color_codes=True) #overide maplot libs ugly colours.
mpl.rcParams['figure.figsize'] = [13, 8] #default figure size

df = pd.read_csv('openrice.csv')
df = df.drop_duplicates('res_id')
df["Like%"] = df["likes"]/(df["likes"] + df["dislikes"])
df['popularity'] = df['Like%']*df["bookmarks"]

df_cuisine = df.groupby('cuisine').mean().sort_values(by = 'popularity', ascending=False)
df_cuisine = df_cuisine.rename(index ={'Shanghai':'Fusion','Taiwan':'Fusion','Brazilian':'Fusion','French':'Fusion','Western':'Fusion','Taiwanese Drink':'Fusion','International':'Fusion'})
df_cuisine = df_cuisine.groupby('cuisine')

df_updated = df_cuisine.mean().sort_values(by = 'popularity', ascending=False)
df_dropped = df_updated.drop(['Group Dining', 'Business Dining', "Wonton/Dumpling", 'Social Enterprise Restaurant'])

df_dropped.popularity.head(10).plot.pie(autopct="%.1f%%", pctdistance=0.5, figsize=(10,10), fontsize=15)
plt.title('Top 10 Most Popular Japanese Restaurants (Filter: Authentic)', fontsize= 20)
plt.ylabel('')

plt.show()
