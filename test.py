import sqlite3

connection = sqlite3.connect("newdb.db")
cursor = connection.cursor()
book_id = input('Book id: ')
book_title = input('Book title: ')
book_year = input('Book year: ')
new_data = ("INSERT INTO Books (ID, title, year) VALUES ('{}','{}', {});".format(book_id, book_title, book_year))
cursor.execute(new_data)
connection.commit()
cursor.execute("SELECT * FROM Books;")
all_results = cursor.fetchall()
print(all_results)
