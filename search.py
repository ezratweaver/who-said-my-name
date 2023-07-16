import requests
import os
from datetime import date
from dotenv import load_dotenv
from database_manager import add_entry, check_for_article

load_dotenv()
api_key = os.environ.get("api")

PROMPT = "Red Wing Scarlet Kitchen and Bar"
FROM_DATE = str(date.today())

def find_articles(prompt: str, from_date: str, api_key: str) -> dict:
    """
    Finds articles based on a prompt and date using the News API.

    Args:
        prompt (str): The search prompt for the articles.
        from_date (str): The starting date to search for articles (YYYY-MM-DD).
        api_key (str): The API key for accessing the News API.

    Returns:
        int: a number that represents the total number of articles found.
        dict: a list of articles that match the prompt given.
    """
    query = f"""https://newsapi.org/v2/everything?q={prompt}&
            from={from_date}&sortBy=publishedAt&apiKey={api_key}"""

    response = requests.get(query)
    data = response.json()
    articles = data.get("articles")
    if articles is None:
        print(response.text)
        quit()
    return data['totalResults'], articles

def sort_article_data(articles: list, add_to_db=True):
    """
    Sorts article data against database of articles, returns number
    of articles not found in that database.

    Args:
        articles (list): A list of articles.
        total_articles (int): The total number of articles.
        add_to_db (bool)(default = True): bool switch for adding nonfound articles
                                            to database.

    Returns:
        int: The updated total number of articles.
        list: Of updated list of articles without duplicates.
    """
    total_articles = len(articles)
    new_article_list = []
    for article in articles:
        article_data = (article["title"], article["publishedAt"], 
                        article["author"], article["source"]["name"], 
                        article["description"], article["url"],
                        article["urlToImage"])
        
        if check_for_article(article_data) is True:
            total_articles-= 1
            continue
        
        new_article_list.append(article_data)

        if add_to_db is True:
            add_entry(*article_data)

    return total_articles, new_article_list

def display_articles(articles: list, display_big_lists=True):
    if len(articles) > 10 and display_big_lists is False:
        raise ValueError("List is To Large!!!!!")
    for article in articles:
        print_article(*article)


def print_article(article_title: str, published_date: str, author: str, 
                                    source_name: str, article_description: str, 
                                    article_url: str, cover_image: str) -> None:
    """
    Prints the metadata of an article.

    Args:
        article_title (str): The title of the article.
        published_date (str): The published date of the article.
        author (str): The author of the article.
        source_name (str): The name of the source.
        article_description (str): The description of the article.
        article_url (str): The URL of the article.
        cover_image (str): The cover image of the article.
    """
    print("---------Article Found!---------")
    print("Article Title:", article_title)
    print("Published Date:", published_date)
    print("Author:", author)
    print("Source Name:", source_name)
    print("Article Description:", article_description)
    print("Article URL:", article_url)
    print("Cover Image:", cover_image)
    print("--------------------------------")


if __name__ == "__main__":
    total_articles, articles = find_articles(PROMPT, FROM_DATE, api_key)
    total_articles, sorted_articles = sort_article_data(articles, add_to_db=False)
    print(f"\n{FROM_DATE}: Total Articles Found: {total_articles}")