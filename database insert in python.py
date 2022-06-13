import sqlite3
#from tkinter.tix import INTEGER, TEXT

cnt = sqlite3.connect('sql.db')
Id INTEGER,
username TEXT,
password TEXT,
email TEXT,
phone TEXT,
usertype TEXT,
status INTEGER,
createddate TEXT,
updateddate TEXT
cnt.execute('''INSERT INTO users VALUES(
 '1','dharma','dharma','purnakarki65652@gmail..com','9848165652','admin','Active','2022/06/13','2022/06/13');''')

