import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('CREATE TABLE users (username TEXT, password TEXT)')
c.execute("INSERT INTO users VALUES ('admin', 'supersecret123')")
conn.commit()
conn.close()

print("Database created with test user: admin / supersecret123")
