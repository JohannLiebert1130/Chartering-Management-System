import sqlite3


def init_db():
    connection = sqlite3.connect('vesseldb.sqlite')

    connection.executescript('''
    DROP TABLE IF EXISTS Vessels;
  DROP TABLE IF EXISTS Orders;
  
    CREATE TABLE Vessels (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    state    INTEGER
    )
    
    CREATE TABLE Orders (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    state    INTEGER,
    bg_time DATA ,
    ed_time DATA ,
    vessel_id INTEGER
    );

    ''')

    for i in range(20):
        connection.execute("INSERT INTO Vessels(state) VALUES(?)", '0')

    connection.commit()

    result = connection.execute("SELECT * FROM Vessels")

    for data in result:
        print("id:", data[0])
        print("state: ", data[1])

    connection.close()


init_db()
