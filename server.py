import json
import sys

import bottle
from bottle import delete
from bottle import get
from bottle import put
from bottle import response
from bottle import request
from bottle import route
from bottle import view
from stevedore import driver

from model import ToDo


mgr = driver.DriverManager('cloaked_archer.db_drivers', sys.argv[1],
                           invoke_on_load=True)
db_driver = mgr.driver


@route('/')
@view('index')
def index():
    """Load index.html with current to-do items"""
    todos = db_driver.get_all()
    return dict(todos=todos)


@get('/todo/<id>')
def todo_get(id):
    t = db_driver.get(id)
    return json.dumps(dict(id=t.id, title=t.title, description=t.description))


@get('/todo')
def todo_get_all():
    """Returns JSON of all to-do items"""
    todos_dict = [dict(id=t.id, title=t.title, description=t.description)
                  for t in db_driver.get_all()]
    return json.dumps(todos_dict)


@put('/todo')
def todo_put():
    todo = ToDo(request.json['title'], request.json['description'])
    db_driver.insert(todo)
    response.status = 201


@delete('/todo/<id>')
def todo_delete(id):
    if db_driver.delete(id):
        response.status = 204
    response.status = 404

bottle.debug(True)
bottle.run(host='localhost', port=8080, reloader=True)
