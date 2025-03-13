from bs4 import BeautifulSoup
import requests
# with open("./website.html") as site:
#     content = site.read()
# soup = BeautifulSoup(content,features="html.parser")
# print(soup.prettify())
response = requests.get("https://news.ycombinator.com/")
html = response.text
soup = BeautifulSoup(html,"html.parser")
anchor_tags = soup.select(".titleline a")
print(anchor_tags)    