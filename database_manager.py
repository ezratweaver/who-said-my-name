import sqlite3

db_connection = sqlite3.connect('found-articles.db')

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM articles")

