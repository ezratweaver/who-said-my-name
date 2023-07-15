import sqlite3

db_connection = sqlite3.connect('found-articles.db')

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM articles")

known_articles = cursor.fetchall()


def check_for_article(article_tuple) -> bool:
    """
    Checks if the given article tuple is known.
    
    Args:
        article_tuple (tuple): The article tuple to check.
        
    Returns:
        bool: True if the article is known, False otherwise.
    """
    for article in known_articles:
        if article_tuple == article:
            return True
    return False

def add_entry(title: str, date: str, author: str, source: str,
                description: str, url: str, image: str) -> None:
    """
    Adds an entry to the articles table in the database.
    
    Args:
        title (str): The title of the article.
        date (str): The published date of the article.
        author (str): The author of the article.
        source (str): The source of the article.
        description (str): The description of the article.
        url (str): The URL of the article.
        image (str): The cover image of the article.
    """
    cursor.execute(f"""INSERT INTO articles
        (article_title, published_date, author, source, 
        article_description, article_url, cover_image)
        VALUES ('{title}', '{date}', '{author}', '{source}', 
        '{description}', '{url}', '{image}')""")
    db_connection.commit()
    db_connection.close()

