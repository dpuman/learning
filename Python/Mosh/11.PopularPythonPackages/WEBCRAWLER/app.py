import requests
from bs4 import BeautifulSoup
response = requests.get("https://stackoverflow.com//questions")
soup = BeautifulSoup(response.text, "html.parser")

quistions = soup.select(".question-summary")

# print(type(quistions[0]))
# print(quistions[0].attrs)
# print(quistions[0].get("id", 0))
# print(quistions[0].select(".question-hyperlink"))
# print(quistions[0].select_one(".question-hyperlink"))
# print(quistions[0].select_one(".question-hyperlink").getText())
for quistion in quistions:
    print(quistion.select_one(".question-hyperlink").getText())
    print(quistion.select_one(".vote-count-post ").getText())
