from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Main.html')

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


@app.route('/acc_user/<username>')
def User_name(username):
    return render_template('hello.html', name = username)

if __name__ == '__main__': #Точка входа нашей программы 
    print("пошел нахуй со своми лабами") 
    app.run(debug=True)
