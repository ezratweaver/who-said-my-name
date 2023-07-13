import requests
import os

from dotenv import load_dotenv

load_dotenv()

prompt = "Red Wing Scarlet Kitchen and Bar"

date = "2023-06-13"

api_key = os.environ.get("api")

query = f"https://newsapi.org/v2/everything?q={prompt}&from={date}&sortBy=publishedAt&apiKey={api_key}"

response = requests.get(query)

data = response.json()
articles = data.get("articles")

print(f"Total Articles Found: {data['totalResults']}")

for article in articles:
    journalist_name = article["source"]["name"]
    author = article["author"]
    article_title = article["title"]
    article_description = article["description"]
    article_url = article["url"]
    cover_image = article["urlToImage"]
    published_date = article["publishedAt"]

    print("--------------------")
    print("Article Title:", article_title)
    print("Published Date:", published_date)
    print("Author:", author)
    print("Journalist Name:", journalist_name)
    print("Article Description:", article_description)
    print("Article URL:", article_url)
    print("Cover Image:", cover_image)

