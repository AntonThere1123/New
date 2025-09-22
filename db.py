import sqlite3

connetion = sqlite3.connect('my_database.db')
cursor = connetion.cursor()

def productDB():
    listDB = cursor.execute('SELECT * FROM product ')
    connetion.close()
    return listDB.fetchall()

