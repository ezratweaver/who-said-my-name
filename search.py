import requests
import os
import sqlite3

from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("api")


PROMPT = "Red Wing Scarlet Kitchen and Bar"
FROM_DATE = "2023-06-13"

def find_articles(prompt, from_date, api_key) -> dict:
    query = f"https://newsapi.org/v2/everything?q={prompt}&from={from_date}&sortBy=publishedAt&apiKey={api_key}"

    response = requests.get(query)
    data = response.json()
    articles = data.get("articles")
    return data['totalResults'], articles

def sort_article_data(articles):
    for article in articles:
        source = article["source"]["name"]
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
        print("Journalist Name:", source)
        print("Article Description:", article_description)
        print("Article URL:", article_url)
        print("Cover Image:", cover_image)


total_results, articles = find_articles(PROMPT, FROM_DATE, api_key)

print(f"Total Articles Found: {total_results}")
sort_article_data(articles)