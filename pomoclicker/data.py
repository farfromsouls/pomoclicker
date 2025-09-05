import sqlite3


db_path = 'pomoclicker/db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    username TEXT PRIMARY KEY,
    money INTEGER,
    upgrade30 INTEGER,
    upgrade45 INTEGER,
    upgrade60 INTEGER
)''')

def getUsers():
    cursor.execute('SELECT username FROM Users')
    users = cursor.fetchall()
    return [user[0] for user in users]

def createUser():
    cursor.execute('''
    INSERT INTO Users (username, money, upgrade30, upgrade45, upgrade60)
    VALUES (?, ?, ?, ?, ?)''', 
    ("username1", 0, 0, 0, 0))
    conn.commit()

def setMoney(money, username):
    cursor.execute('UPDATE Users SET money = ? WHERE username = ?', (money, username, ))
    conn.commit()

def getMoney(username):
    cursor.execute('SELECT money FROM Users WHERE username = ?', (username, ))
    money = cursor.fetchone()
    return money[0]