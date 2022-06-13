import sqlite3
cnt = sqlite3.connect('sql.db')
cnt.execute('''CREATE TABLE users(
id INTEGER,
username TEXT,
password TEXT,
email TEXT,
phone TEXT,
usertype TEXT,
status INTEGER,
createddate TEXT,
updateddate TEXT
);''')