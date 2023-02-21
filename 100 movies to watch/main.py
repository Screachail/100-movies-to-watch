import requests
from bs4 import BeautifulSoup
import spotipy


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
page_text = response.text

soup = BeautifulSoup(page_text, "html.parser")

span = soup.find_all("h3", class_="title")

movies = []
x = 99
for title in span:
    movies += title

movies.reverse()

with open ("100movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie + "\n")