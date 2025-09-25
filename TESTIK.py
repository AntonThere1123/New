from flask import Flask, render_template, request

app = Flask(__name__)

Acc=False

@app.route('/MyOffice', methods = ['POST', 'GET'])
def integer():
    messeg =''
    if request.method == "POST":
        user = request.form.get('user')
        password =request.form.get('password')
        messeg = messeg + user + '' + password
        return render_template('Office.html', messeg= messeg)
    
    return render_template('Office.html', messeg="Вы не зареганы")


if __name__== '__main__':
    print('run server')
    app.run()