import sqlite3
import time
from functions import Book

conn = sqlite3.connect('data.db')

c = conn.cursor()

#   This code create a table in our database
# c.execute("""CREATE TABLE book (
#             code text,
#             name text,
#             publisher text,
#             year integer,
#             price real
#             )""")

book_1 = Book('10001', 'Neuromancer: 1', 'Aleph', 2016, 24.89)
book_2 = Book('10111', 'Count Zero: 2', 'Aleph', 2017, 26.99)

# This code inserts data to the db file

# In this way we pass a tuple to the db
# c.execute("INSERT INTO book VALUES (?, ?, ?, ?, ?)", (
#    book_1.code,book_1.name,book_1.publisher,book_1.year,book_1.price))

# This code will confirm the insertion
# conn.commit()

# In this way we pass a dictionary to the db
# c.execute("INSERT INTO book VALUES (:code, :name, :publisher, :year, :price)",
#        {'code':book_2.code,'name':book_2.name,'publisher':book_2.publisher,'year':book_2.year,'price':book_2.price})

c.execute("SELECT * FROM book WHERE publisher='Aleph'")

# This will return the values into "SELECT[...]"

data = c.fetchall()
n = 0
for n in range(len(data)):
    in_data = data[n]
    if n != 0:
        print('--'*3)
    print(type(data[n]))
    for y in range(len(in_data)):
        print(in_data[y])
        y += 1
        time.sleep(0.3)


conn.commit()

conn.close()
