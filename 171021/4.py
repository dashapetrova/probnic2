from flask import Flask
from flask import request
from flask import render_template
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    prizes=['котика','хомяка']
    prize = choice(prizes)
    return render_template('3.html', prize=prize)

@app.route('/hi')
def hi():
    if 'name' in request.args:
        name = request.args['name']
        return '<html><body><h1>Hi, {}!</h1></body></html>'.format(name)
    else:
        return '<html><body><h1>Input name.</h1></body></html>'

if __name__=='__main__':
    app.run(debug=True)
