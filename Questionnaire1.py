from flask import Flask, render_template, request, url_for, flash, redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '143f01ce9dfec75fc40fb978d680fa20c43a753689c44ab7'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route('/')
def index():
    return render_template('Index.html', messages=messages)


@app.route('/create')
def create():
    return redirect(url_for(''))


@app.route('/create/<name>', methods=('GET', 'POST'))
def create_with_id(name=None):
    if request.method == 'POST':
        print('POST')
        title = request.form['title']
        content = request.form['content']

        if not title and not content:
            flash('Title is required!')
            flash('Content is required!')
            print('No Title and No Content')
        elif not title:
            flash('Title is required!')
            print('No Title')
        elif not content:
            flash('Content is required!')
            print('No content')
        else:
            messages.append({'title': title, 'content': content})
            print('Title & Content')
            return redirect(url_for('index'))
    print('Get')
    return render_template('create.html', name=name)

