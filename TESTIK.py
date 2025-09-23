from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['post', 'get'])
def integer():
    messeg =''
    if request.method == "POST":
        user = request.form.get('user')
        password =request.form.get('password')
        messeg = messeg + user + '' + password
        return render_template('TESTIK.html', messeg= messeg)
    
    return render_template('TESTIK.html', messeg="Хз")


if __name__== '__main__':
    print('run server')
    app.run()