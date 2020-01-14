import mysql.connector
from cryptography.fernet import Fernet
from json import load

file = open('.key','rb')
key = file.read()
file.close()


fh = {}

with open("config.json") as json_file:
	x = load(json_file)
	fh = x


def check(service):
    connection = mysql.connector.connect(
								host=fh["host"],
								user=fh["user"],
								password=fh["password"]
				)
    crsr = connection.cursor()
    query = "Select * from {}.password where name={}".format(fh["user"],service_name.lower())
    crsr.execute(query)
    ans = crsr.fetchall()

    if ans==[]:
        return False

    return True

def insert(service_name, password):
    connection = mysql.connector.connect(
								host=fh["host"],
								user=fh["user"],
								password=fh["password"]
				)
    crsr = connection.cursor()
    password = password.encode()
    f = Fernet(key)
    password = f.encrypt(password)
    query = "Insert into {}.password (name,password) \
                values ({},{})".format(fh["user"],service_name.lower(),password)
    crsr.execute(query)
    connection.commit()
    connection.close()


def update(service_name, password):
    if check(service_name)==False:
        insert(service_name,password)
    else:
        connection = mysql.connector.connect(
								host=fh["host"],
								user=fh["user"],
								password=fh["password"]
				)
        crsr = connection.cursor()
        password = password.encode()
        f = Fernet(key)
        password = f.encrypt(password)
        print(password)
        query = "Update {}.password set password={} where name={}".format(fh["user"],password,service_name.lower())
        crsr.execute(query)
        connection.commit()
        connection.close()

def displayTable():
    connection = mysql.connector.connect(
								host=fh["host"],
								user=fh["user"],
								password=fh["password"]
				)
    crsr = connection.cursor()
    query = "Select * from {}.password;".format(fh["user"])
    crsr.execute(query)
    ans = crsr.fetchall()
    final_ans = []
    for i in ans:
        password = i[-1]
        f = Fernet(key)
        # print(password)
        password = f.decrypt(password.encode('utf-8')).decode('utf-8')
        final_ans.append((i[0],i[1],password))
    print(final_ans)

if __name__ == '__main__':
    displayTable()

