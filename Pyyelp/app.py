import requests
import config

url= "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term" : "Barber",
    "location" : "NYC"
}

response = requests.get(url, headers=headers, params=params)
#print(response.text)
businesses = response.json()["businesses"] #to have a list of dictionaries
#for business in businesses:
 #   print(business["name"])

names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)