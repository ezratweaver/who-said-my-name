import requests
import os
from datetime import date
from dotenv import load_dotenv
from database_manager import add_entry, check_for_article

load_dotenv()
api_key = os.environ.get("api")


PROMPT = "Red Wing Scarlet Kitchen and Bar"
FROM_DATE = str(date.today())
FROM_DATE = "2023-06-13"

def find_articles(prompt, from_date, api_key) -> dict:
    query = f"https://newsapi.org/v2/everything?q={prompt}&from={from_date}&sortBy=publishedAt&apiKey={api_key}"

    response = requests.get(query)
    data = response.json()
    articles = data.get("articles")
    if articles is None:
        print(response.text)
        quit()
    return data['totalResults'], articles

def sort_article_data(articles):
    for article in articles:
        article_data = (article["title"], article["publishedAt"], 
                        article["author"], article["source"]["name"], 
                        article["description"], article["url"],
                        article["urlToImage"])
        
        if check_for_article(article_data):
            continue

        print("--------------------")
        print("Article Title:", article_data[0])
        print("Published Date:", article_data[1])
        print("Author:", article_data[2])
        print("Source Name:", article_data[3])
        print("Article Description:", article_data[4])
        print("Article URL:", article_data[5])
        print("Cover Image:", article_data[6])


total_results, articles = find_articles(PROMPT, FROM_DATE, api_key)

print(f"{FROM_DATE}: Total Articles Found: {total_results}")

sort_article_data(articles)