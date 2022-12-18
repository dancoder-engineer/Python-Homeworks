import urllib.request, urllib.parse, urllib.error
import sqlite3
import json


fileName = "roster_data.json"
rawJson = open(fileName).read()
js = json.loads(rawJson)

conn = sqlite3.connect('studentdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS User')
cur.execute('DROP TABLE IF EXISTS Course')
cur.execute('DROP TABLE IF EXISTS Member')

cur.execute('CREATE TABLE User(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Name TEXT UNIQUE)')
cur.execute('CREATE TABLE Course(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE)')
cur.execute('CREATE TABLE Member(user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_id))')




for entry in js:
    print(entry)
    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES (?)', (entry[1],))
    cid = cur.execute('SELECT id FROM Course where title = ?',(entry[1],))
    course_id = cur.fetchone()[0]


    cur.execute('INSERT OR IGNORE INTO User(Name) VALUES (?)',(entry[0],) )
    uid = cur.execute('SELECT id FROM User WHERE Name = ?', (entry[0],))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT INTO Member(user_id, course_id, role) VALUES(?, ?, ?)', (user_id, course_id, entry[2]))

# a = cur.execute('SELECT * FROM User')
# for i in a:
#     print(i)

conn.commit()