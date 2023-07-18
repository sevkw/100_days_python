from bs4 import BeautifulSoup
import requests

website = "https://news.ycombinator.com/"

response = requests.get(website)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.text
    article_texts.append(article_text)
    link = article_tag.find("a")["href"]
    article_links.append(link)

article_upvotes = [ int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score") ]

max_upvote = max(article_upvotes)

max_upvote_index = article_upvotes.index(max_upvote)

print(max_upvote, max_upvote_index)
print(article_texts[max_upvote_index], article_links[max_upvote_index])
