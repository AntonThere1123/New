from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world 1'

if __name__ == '__main__': #Точка входа нашей программы 
    print("Привет мир!") 
    app.run(debug=True)
