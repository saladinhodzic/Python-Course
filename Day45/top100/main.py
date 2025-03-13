from bs4 import BeautifulSoup
import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html = response.text
soup = BeautifulSoup(html,"html.parser")
h3_list = soup.find_all(name="h3",class_="title")[::-1]
movie_list = [movie.getText() for movie in h3_list]
with open("movies.txt",'a',encoding="utf-8") as top100:
    for movie in movie_list:
        top100.write(f"{movie}\n")
