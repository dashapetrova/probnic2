from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>Hello,world!</h1></body></html>'

@app.route('/hi')
def hi():
    if 'name' in request.args:
        name = request.args['name']
        return '<html><body><h1>Hi, {}!</h1></body></html>'.format(name)
    else:
        return '<html><body><h1>Input name.</h1></body></html>'
if __name__=='__main__':
    app.run(debug=True)
