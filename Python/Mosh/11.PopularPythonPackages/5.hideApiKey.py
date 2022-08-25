import requests
import config
url = "https://api.yelp.com/v3/businesses/search"

header = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "location": "NYC",
    "term": "Barber"

}
response = requests.get(url, headers=header, params=params)
businesses = response.json()['businesses']
busnes = [busines["name"]
          for busines in businesses if busines['rating'] > 4.5]

for bs in busnes:
    print(bs)

# for busnes in businesses:
#     print(busnes['name'])
