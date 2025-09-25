from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/MyOffice', methods=['GET', 'POST'])
def my_office():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Здесь можно добавить проверку подлинности учетных данных
        logged_in = True
        message = f'Добро пожаловать, {username}'
    else:
        message = 'Вы не зарегистрированы.'
    return render_template('Office.html', message=message)

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Сохранение регистрационных данных (например, в базу данных)
        # Примечание: Это упрощённая версия, реальная регистрация должна включать хранение хэшей паролей и защиту от SQL инъекций
        return redirect(url_for('my_office'))
    return render_template('Register.html')

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