from flask import Flask
from flask import url_for
from markupsafe import escape
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


def valid_login(username, password):
    pass


@app.route('/hello/')
@app.route('/hello/<name>')
def log_the_user_in(name=None):
    return render_template('Hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
