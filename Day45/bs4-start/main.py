from bs4 import BeautifulSoup
with open("./website.html") as site:
    content = site.read()
soup = BeautifulSoup(content,features="html.parser")
print(soup.prettify())