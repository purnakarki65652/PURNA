import sqlite3
cnt = sqlite3.connect('sql.db')
cnt.execute('''INSERT INTO users (id, username, password, email, phone,usertype,status,createddate) VALUES(
'1','Purna','karki','purnakarki65652@gmail.com','9848165652','admin','1','2022-06-15'
);''')
cur = cnt.cursor()
cnt.commit()