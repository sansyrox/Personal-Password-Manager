import mysql.connector
from json import load as json_load

fh = {}
with open("config.json") as json_file:
	x = json_load(json_file)
	fh = x

connection = mysql.connector.connect(
								host=fh["host"],
								user=fh["user"],
								password=fh["password"]
				)
cursr = connection.cursor()

cursr.execute("""create table %s.password(
                id INTEGER primary key Auto_Increment,
                name varchar(30) Not Null,
                password varchar(200)
                );""",(fh["user"]))


connection.commit()
connection.close()



