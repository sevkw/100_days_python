from bs4 import BeautifulSoup
import requests

website = "https://web.archive.org/web/20200515133712/https://www.empireonline.com/movies/features/best-movies-2/"

movie_text = requests.get(website).text

soup = BeautifulSoup(movie_text, "html.parser")

movies = soup.find_all(name="h3", class_="title")

movie_titles = [ movie.text for movie in movies]
# or movie_titles[::-1]
movie_titles.reverse()

with open("movies.txt", mode="w",  encoding="utf8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")

