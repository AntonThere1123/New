from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

connetion = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connetion.cursor()

def productDB():
    listDB = cursor.execute('SELECT * FROM product ')
    return listDB.fetchall()

@app.route('/')
def index():
    shop= productDB()
    return render_template('Main.html', shop =shop)

@app.route('/News')
def News():
    return render_template('News.html')

@app.route('/News/Promo')
def Promo():
    return 'Акции лол'

@app.route('/News/Announcements')
def Announcements():
    return 'Анонсы'

@app.route('/Products')
def Products():
    return render_template('Product.html')

@app.route('/Products/Accessories')
def Accessories():
    return 'Аксесуары'

@app.route('/MyOffice')
def My_Office():
    return render_template('Office.html')

@app.route('/About_us')
def About_us():
    return render_template('About_us.html')


@app.route('/Contacts')
def Contacts():
    return render_template('Contacts.html')



@app.route('/acc_user/<username>')
def User_name(username):
    return render_template('hello.html', name = username)

if __name__ == '__main__': #Точка входа нашей программы 
    print("Hi") 
    app.run(debug=True)
