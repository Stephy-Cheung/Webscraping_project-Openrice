import pandas as pd

# Screen out restuarants with less than 5 reviews
df = pd.read_csv('openrice.csv')
df = df.drop_duplicates(subset ='res_id')
df = df[df['review']>5]

# Create new column for 'District'
df['District']=df['address'].apply(lambda x: x.split(',')[-1])

# Create new column for 'Like%'
df['Like%'] = df'likes']/(df['dislikes']+df['likes'])*100

# Change invalid input in 'District' to correct location 
print(df[df['District']=='2及15號舖'].index)
df.loc[68, 'District'] = 'Western District'

# Update restuarnt provide cusisine more than one location to 'fusion'
df_cuisine = df.groupby('cuisine').mean().sort_values('Popularity',ascending = False)
df_cuisine
df_cuisine = df_cuisine.rename(index ={'Shanghai':'Fusion','Taiwan':'Fusion','Brazilian':'Fusion','French':'Fusion','Western':'Fusion','Taiwanese Drink':'Fusion','International':'Fusion'})
df_cuisine = df_cuisine.groupby('cuisine')
df_cuisine.mean().sort_values('Popularity',ascending=False)
