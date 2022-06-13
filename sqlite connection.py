import sqlite3
try:
    sqliteConnection = sqlite3.connect('sql.db')
    cursor = sqliteConnection.cursor()
    print('DB Intl')
    qurey = 'select sqlite_version();'
    cursor.execute(qurey)
    result = cursor.fetchall()
    print('SQLite Verson is{}'.format(result))
    cursor.close()
except sqlite3.Error as error:
    print('Error occured -',error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite connection is closed')