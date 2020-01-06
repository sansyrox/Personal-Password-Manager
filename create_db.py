import sqlite3

connection = sqlite3.connect("myTable.db")
cursr = connection.cursor()

cursr.execute("""create table password(
                id INTEGER primary key ,
                name varchar(30),
                password varchar(200)
                );""")


connection.commit()
connection.close()



