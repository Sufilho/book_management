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
book_3 = Book('13101', 'Monalisa Overdrive: 3 ', 'Aleph', 2017, 26.00)
book_4 = Book('13101', 'Do Androids Dream of Electric Sheep? Vol. 1', 'Aleph', 2009, 29.86)

# The code bellow inserts data to the db file
# In this way we pass a tuple to the db

# c.execute("INSERT INTO book VALUES (?, ?, ?, ?, ?)", (
#    book_1.code,book_1.name,book_1.publisher,book_1.year,book_1.price))

# The code bellow pass a dictionary to the db

# c.execute("INSERT INTO book VALUES (:code, :name, :publisher, :year, :price)",
#        {'code':book_4.code,'name':book_4.name,'publisher':book_4.publisher,'year':book_4.year,'price':book_4.price})

c.execute("SELECT * FROM book WHERE publisher='Aleph'")

# The code bellow will return the values into "SELECT[...]"

data = c.fetchall()

print(data) # data will be a list of tuples
b = 0
for b in range(len(data)):
    book_data = data[b]
    if b != 0:
        print('--'*3)
    print(type(data[b]))
    for item in range(len(book_data)):
        print(book_data[item])
        # item += 1
        time.sleep(0.3)

# The code bellow will confirm the cursor action

conn.commit()

conn.close()
