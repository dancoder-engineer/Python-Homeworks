import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS domains')
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('''
    CREATE TABLE counts (org TEXT, count INTEGER)''')

f=open("mbox.txt", "r")

for line in f:
    if not line.startswith('From: '): continue
    domain = line.split()[1].split('@')[1]
    cur.execute('SELECT * FROM counts WHERE org = ?', (domain,) )
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO counts(org, count) VALUES(?, 1)',(domain,))
    else:
        cur.execute('UPDATE counts SET count = count + 1 WHERE org = ?', (domain,))
    conn.commit()