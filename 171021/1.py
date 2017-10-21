from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>Hello,world!</h1></body></html>'

@app.route('/hi')
def hi():
    return '<html><body><h1>Hi!</h1></body></html>'

if __name__=='__main__':
    app.run(debug=True)
