from flask import Blueprint, render_template, url_for, redirect, request, current_app
from bson.objectid import ObjectId


main = Blueprint('main', __name__)

@main.get('/')
def index():
    todos = current_app.db.todos.find()

    return render_template('index.html', todos=todos)

@main.post('/add_todo')
def add_todo():
    todo_item = request.form.get('add-todo')
    current_app.db.todos.insert_one({'text': todo_item, 'complete': False})

    return redirect(url_for('main.index'))

@main.route('/complete_todo/<oid>')
def complete_todo(oid):
    todo_item = current_app.db.todos.find_one({'_id': ObjectId(oid)})
    current_app.db.todos.update_one(todo_item, {'$set': {'complete': True}})

    return redirect(url_for('main.index'))

@main.route('/delete_completed/')
def delete_completed():
    current_app.db.todos.delete_many({'complete': True})

    return redirect(url_for('main.index'))

@main.route('/delete_all/')
def delete_all():
    current_app.db.todos.delete_many({})

    return redirect(url_for('main.index'))
