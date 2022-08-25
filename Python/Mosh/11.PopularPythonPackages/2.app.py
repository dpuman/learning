import requests
url = "https://api.yelp.com/v3/businesses/search"
api_key = "ZiCk9r8Yhij_DEx7a5USpKqXNVaZkAMq6jywIajZcGQu_j0hhLH9Skfi-S5wi87CesAj6SJnDMzW4uNeJc17wwa0O15HrGeacNW9KxnqBhnGRZ3JA1NtNH9NRqrnXnYx"
header = {
    "Authorization": "Bearer "+api_key
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
