import sqlite3


def init_db():
    connection = sqlite3.connect('logindb.sqlite')

    connection.executescript('''
    DROP TABLE IF EXISTS Users;
    
    CREATE TABLE Users (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE,
    email    TEXT UNIQUE,
    password TEXT
    );
                           
    ''')

    connection.execute("INSERT INTO Users(name,email,password) VALUES(?,?,?)", ('Johann', 'test@qq.com', '690527'))

    connection.commit()

    result = connection.execute("SELECT * FROM USERS")

    for data in result:
        print("id",data[0])
        print("Username : ", data[1])
        print("Email : ", data[2])
        print("Password :", data[3])

    connection.close()


init_db()
