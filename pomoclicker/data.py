import sqlite3


db_path = 'pomoclicker/db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    username TEXT PRIMARY KEY,
    money INTEGER DEFAULT 0,
    
    sessions30 INTEGER DEFAULT 0,
    sessions45 INTEGER DEFAULT 0,
    sessions60 INTEGER DEFAULT 0,

    upgrade30 INTEGER DEFAULT 0,
    upgrade45 INTEGER DEFAULT 0,
    upgrade60 INTEGER DEFAULT 0
)''')

cursor.execute('SELECT username FROM Users WHERE username = ?', ("user", ))
user = cursor.fetchone()

if user == None:
    cursor.execute('''
    INSERT INTO Users (username)
    VALUES (?)''',
    ("user", ))
    conn.commit()

def setMoney(money: int) -> None:
    cursor.execute('UPDATE Users SET money = ? WHERE username = "user"', (money, ))
    conn.commit()

def getMoney() -> int:
    cursor.execute('SELECT money FROM Users WHERE username = ?', ("user", ))
    money = cursor.fetchone()
    return money[0]

def setMileAge(mode: int) -> None:
    cursor.execute(f'UPDATE Users SET "sessions{mode}" = "sessions{mode}" + 1'
                   +' WHERE username = ?', ("user", ))
    conn.commit()

def getMileAge() -> list[int]:
    cursor.execute('SELECT sessions30, sessions45, sessions60 FROM Users WHERE username = ?', ("user", ))
    mileage = cursor.fetchone()
    return mileage