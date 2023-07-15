import sqlite3

db_connection = sqlite3.connect('found-articles.db')

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM articles")

known_articles = cursor.fetchall()


def check_for_article(article_tuple):
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

def add_entry(title, date, author, source, description, url, image):
    cursor.execute(f"""INSERT INTO articles
        (article_title, published_date, author, source, 
        article_description, article_url, cover_image)
        VALUES ('{title}', '{date}', '{author}', '{source}', 
        '{description}', '{url}', '{image}')""")
    db_connection.commit()
    db_connection.close()

