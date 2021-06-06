from sqlite3 import *
from datetime import datetime

class DBOperations:
    
    def __init__(self, db_name='newdb.db'):
        self.name = db_name
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        try:
            return connect(self.name)
        except Error as e:
            pass

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        
    def insert(self):
        book_id = input('Book id: ')
        book_title = input('Book title: ')
        book_year = input('Book year: ')
        
        try:
            id = int(book_id)
            year = int(book_year)
        except ValueError:
            print("ERROR:  bookd id or year is not number")
            return
        
        currentYear = datetime.now().year
        
        if year < 0 or year > currentYear:
            print("ERROR: incorrect value for year")
            return
        
        new_data = ("INSERT INTO Books (ID, title, year) VALUES ('{}','{}', {});".format(book_id, book_title, book_year))
        try:
            self.cursor.execute(new_data)
            self.conn.commit()
            print("the entered values have been inserted")
            
        except Error as e:
            print("ERROR: " + str(e))
        
    def select(self):
        self.cursor.execute("SELECT * FROM Books;")
        all_results = self.cursor.fetchall()
        print(all_results)
        
if __name__ == "__main__":
    db_op = DBOperations()
    
    while(True):
        print ("Type I for insert , S for select or X ");
        char_read = input('Enter Your Characters\n')[0].upper()
        if(char_read == 'I'):
            print("Insert record")
            db_op.insert()
        elif(char_read == 'S'):
            print("Show of recods:")
            db_op.select()
        elif(char_read == 'X'):
            print("EXIT")
            break
        else:
            print("Repeat the reading because the option read is not among the three possible ones")
