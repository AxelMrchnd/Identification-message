from flask import Flask, render_template, request, url_for, flash, redirect
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '143f01ce9dfec75fc40fb978d680fa20c43a753689c44ab7'

messages = [
    {
        'title': 'Message One',
        'content': 'Message One Content',
        'sender': 'X',
        'date': 'Il n\'y a pas longtemps',
        'n°ID': '1'
    },
    {
        'title': 'Message Two',
        'content': 'Message Two Content',
        'sender': 'X',
        'date': 'Il n\'y a pas longtemps',
        'n°ID': '2'
    }
            ]


@app.route('/')
def not_exist_yet():
    return redirect(url_for('index', name='RandomUser', viewAll='Yep'))


@app.route('/messages/view', methods=('GET', 'POST'))
def index():
    name = request.args.get('name', '')
    viewAll = request.args.get('viewAll', '')
    if request.method == 'POST':
        ID = request.form.get('ID')
        print(ID)
        return redirect(url_for('modify_message', name=name, viewAll='Iie', ID=str(ID)))
    print(name, viewAll)
    return render_template('Index.html', messages=messages, name=name, viewAll=viewAll)


@app.route('/messages/make', methods=('GET', 'POST'))
def create_with_id():
    name = request.args.get('name', '')
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
            if name == '':
                name = 'X'
            date = datetime.datetime.today().strftime('le %d/%m/%Y à %H:%M %S\'')
            messages.append({'title': title, 'content': content, 'sender': name, 'date': date,
                             'n°ID': str((len(messages) + 1))})
            print('Title & Content')
            return redirect(url_for('index', name=name, viewAll='Yep'))
    print('Get fait')
    return render_template('create.html', name=name)


@app.route('/message/modify', methods=('GET', 'POST'))
def modify_message():
    ID = int(request.args.get('ID', '')) - 1
    name = messages[ID]['sender']
    if request.method == 'POST':
        print('POST')
        title = request.form['title']
        content = request.form['content']

        if not title and not content:
            flash('Title OR Content is required!')
            print('No Title and No Content')
            return render_template('modifier.html', name=name)
        elif not title:
            title = messages[ID]['title']
        elif not content:
            content = messages[ID]['content']
        if name == '':
            name = 'X'
        date = datetime.datetime.today().strftime('le %d/%m/%Y à %H:%M %S\'')
        messages[ID] = {'title': title, 'content': content, 'sender': name, 'date': date, 'n°ID': (ID + 1)}
        print('Title & Content')
        name = request.args.get('name', '')
        return redirect(url_for('index', name=name, viewAll='Yep'))
    print('Get fait')
    return render_template('modifier.html', name=name)
