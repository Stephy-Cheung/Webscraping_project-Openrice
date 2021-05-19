import requests
import re
import pandas as pd
from bs4 import BeautifulSoup


def obtain_info(soup):
    # loop through the pages
    while True:

        # find id in one page
        items = soup.select(".content-wrapper")
        
        for i in items:
            dictionary["res_id"].append(i.find(class_="openrice-bookmark")["data-poi-id"])
            dictionary["address"].append(i.find(class_='icon-info address').text.strip("\n\r"))
            dictionary["likes"].append(i.find(class_='score score-big highlight').text if i.find(class_='score score-big highlight') else 0)
            dictionary["dislikes"].append(i.find(class_='score highlight').text if i.find(class_='score highlight') else 0)
            dictionary["bookmarks"].append(i.find(class_="bookmarkedUserCount").attrs['data-count'])
            dictionary["price_range"].append(i.find(class_="icon-info-food-price").span.text)
            dictionary["cuisine"].append(i.select(".condition_tag_40x40_desktop ~ li")[1].text if len(i.select(".condition_tag_40x40_desktop ~ li")) > 1 else "Not Specified")
            dictionary["review"].append(re.search("\d+",i.find(class_="counters-container").text).group() if i.find(class_="counters-container") else 0)
        
        # find next page
        nextbtn = soup.find(class_="common_pagination_more_r_desktop")

        if nextbtn:
            nextlink = nextbtn.parent["href"]
            subhtml = requests.get("https://www.openrice.com" + nextlink,headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(subhtml.text, "html.parser")
        else:
            break
    return dictionary 

# dictionary for require information of each restuarant
dictionary = {
    "res_id": [],
    "address": [],
    "likes": [],
    "dislikes": [],
    "bookmarks": [],
    "price_range": [],
    "cuisine": [],
    "review": []
}

# location id except Causeway Bay
districtIds = [1008, -35243, -35244, -35242, 1001, 1003, -9006, -9007, 1005, 1002, 1011, 1022, 1017, 1019, 1025, 1026, 1004, 1014, 1023, 1009, 1018, 1024, 1013, 1021, -9151, 1012, 1020, 1016, 1027, 1015, 1007, 1010]

priceRange = ["&priceRangeId=1&priceRangeId=2&priceRangeId=3", "&priceRangeId=4&priceRangeId=5&priceRangeId=6"]

for q in priceRange: 
    for p in districtIds: 
        URL = "https://www.openrice.com/en/hongkong/restaurants?cuisineId=2009&districtId=" + str(p) + q
        html = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(html.text,"html.parser")
        restaurant_info = obtain_info(soup)

# obtain info for Causeway Bay 
URL_list= ["https://www.openrice.com/en/hongkong/restaurants?cuisineId=2009&districtId=1019&priceRangeId=1&priceRangeId=2&priceRangeId=3","https://www.openrice.com/en/hongkong/restaurants?cuisineId=2009&districtId=1019&priceRangeId=4&priceRangeId=5&priceRangeId=6"]
for index, URL in enumerate(URL_list): 
    html = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(html.text,"html.parser")
    restaurant_info = obtain_info(soup)    

df = pd.DataFrame(restaurant_info)

# save data in csv
df.to_csv("openrice.csv",index=False)