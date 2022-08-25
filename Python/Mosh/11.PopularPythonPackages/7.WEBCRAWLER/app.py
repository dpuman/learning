# If a website dosent have an API
import requests
from bs4 import BeautifulSoup
response = requests.get("https://stackoverflow.com//questions")
soup = BeautifulSoup(response.text, "html.parser")

quistions = soup.select(".s-post-summary")

print(type(quistions[0]))
print(quistions[0].attrs)
print(quistions[0].get("id", 0))

print(quistions[0].select(".s-link"))
print(quistions[0].select_one(".s-link"))
print(quistions[0].select_one(".s-link").getText())

for quistion in quistions:
    print(quistion.select_one(".s-link").getText())
    print(quistion.select_one(".s-post-summary--stats-item-number").getText())
