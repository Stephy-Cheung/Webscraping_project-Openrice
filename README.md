(Banner)

# Web-scrapping project on Openrice

This is my first project using Python. We use web-scraping to collect restaurant data from Openrice.com,Hong Kong's most popular dining guide, and provide business advise for new restaurant opening.

## Table of Contents

- [Project background & aim](#roject_background_&_aim)
- [Data Collection](#Data_Collection)
- [Data Preprocessing](#Data_Preprocessing)
- [Assumption](#Assumption)
- [Analysis](#Analysis)
- [Conclusion](#Conclusion)
- [Challenge](#Challenge)
- [Room for Improvement & future application](#Room_for_Improvement)


## Project_background_&_aim
In this project, we are a group of consultants that offer advice to help our client, a Japanese Food Inc, to open a Japanese restaurant on the Hong Kong Island. We will use web scraping to understand the Japanese restaurant market on the Hong Kong Island and provide suitable business advice on the restaurant location, menu price range and types of Japanese food. <br>

Our aim is to provide suggestion for the most profitable combination of restaurant location, menu price range and types of Japanese food for the new restaurant.

## Data_Collection
Web scraping was preformed on the search result of Japanese restaurant on Hong Kong Island on Openrice.com. <br>

(example)

Here is an example of the restaurant information that provided from that search result. For each restaurant, we collected the below data for our analysis
- Restaurant ID (unique)
- Address (location) 
- No. of bookmarks
- Price range
- Likes / dislikes 
- Cuisine
- No. of reviews

(code_restaurant_info)

## Data Preprocessing & assumption
In data preprocessing, duplicated data was dropped according to unqiue res_id provide on Openrice.com and we have screened out restaurant that with number of reviews less than 5. <br>
(code_preprocessing)

The location district is extracted from the English address. However, there are restaurant that only provide Chinese address which cannot be processed. We look into each Chinese address and classified the Distric manually. <br>
(code_address)

We also discovered that the cuisine column returns another locations since they provide fusion cuisine. The invalid entries is changed to 'fusion manually'<br>
(code_preprocess_cuisine)

## Assumption
Since the finance performance of individual restaurant is not available, we have assumed that the more popular the restuarnt is, the higher the profitability. <br>
In our target data, Number of 'likes', 'dislikes', 'bookmarks' and 'review' reflected the popularity of the restaurant. Since we found there is high correlation for 'bookmarks' and 'review'. We create the popularity index as below for analysis.  

Popularity Index = Number of bookmarks x Like precentage

## Analysis
### 1. Location
Causeway Bay, Central, Sheung Wan, Wan Chai, Repulse Bay are the top 5 location for Japanese restaurant popularity index. 
(analysis_location)

### 2. Price range
High menu pricing of above HK$800 per pax has the highest popularity.
(analysis_price range)

### 3. Cuisine
The all-you-can-eat restaurant has the highest popularity in cuisine.
(analysis_cuisine)

## Conclusion
As a conclusion, we would recommend our client to open the new restaurant as an all-you-can-eat Japanese restaurant with a price-range of HK$800 or above. In location, we would like to provide the top 5 location of Causeway Bay, Central, Sheung Wan, Wan Chai and Repulse Bay as consideration as there are large number of Japanese restaurant in location like Causeway Bay and Central and the market may be saturated.

## Challenge
1. Number of returns on each search - We discover that Openrice.com only returne 250 entries for each search and therefore, we have separate the web-scrapping process in batches, followed by drop duplicates to obtain the full dataset.

2. Invalid entries - Invalid entries in 'District' and 'cuisine' found and amended manually during data processing. 

## Room for Improvement & future application
For further enhance the project, a more sophisticated model is requiered to better evaluate the profitability and popularity of the restaurants. Condider additional data source such as website like TripAdvisor, revenue performance of individual restaurant and timeframe of the reviews would further improve the validity of our analysis.  <br>

The above analysis can be applied on various cuisine and locations in Hong Kong to assist different restaurants.

