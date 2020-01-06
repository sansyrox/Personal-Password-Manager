import sqlite3
from cryptography.fernet import Fernet

file = open('.key','rb')
key = file.read()
file.close()

def check(service):
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    crsr.execute("""Select * from password where name=?""",(service_name.lower()))
    ans = crsr.fetchall()

    if ans==[]:
        return False

    return True

def insert(service_name, password):
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    password = password.encode()
    f = Fernet(key)
    password = f.encrypt(password)
    crsr.execute("""Insert into password (name,password)
                values (?,?)""",(service_name.lower(),password))
    connection.commit()
    connection.close()


def update(service_name, password):
    if check(service_name)==False:
        insert(service_name,password)
    else:
        connection = sqlite3.connect("myTable.db")
        crsr = connection.cursor()
        password = password.encode()
        f = Fernet(key)
        password = f.encrypt(password)
        print(password)
        crsr.execute("""Update password set password=? where
                    name=?""",(password,service_name.lower()))
        connection.commit()
        connection.close()

def displayTable():
    connection = sqlite3.connect("myTable.db")
    crsr = connection.cursor()
    crsr.execute("Select * from password;")
    ans = crsr.fetchall()
    final_ans = []
    for i in ans:
        password = i[-1]
        f = Fernet(key)
        password = f.decrypt(password).decode()
        final_ans.append((i[0],i[1],password))
    print(final_ans)

if __name__ == '__main__':
    displayTable()
