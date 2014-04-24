import json

import bottle
from bottle import delete
from bottle import get
from bottle import put
from bottle import response
from bottle import request
from bottle import route
from bottle import view

from model import ToDo


from driver_memory import MemoryDriver
driver = MemoryDriver()


@route('/')
@view('index')
def index():
    """Load index.html with current to-do items"""
    todos = driver.get_all()
    return dict(todos=todos)


@get('/todo/<id:int>')
def todo_get(id):
    t = driver.get(id)
    return json.dumps(dict(id=t.id, title=t.title, description=t.description))


@get('/todo')
def todo_get_all():
    """Returns JSON of all to-do items"""
    todos_dict = [dict(id=t.id, title=t.title, description=t.description)
                  for t in driver.get_all()]
    return json.dumps(todos_dict)


@put('/todo')
def todo_put():
    todo = ToDo(request.json['title'], request.json['description'])
    driver.insert(todo)
    response.status = 201


@delete('/todo/<id:int>')
def todo_delete(id):
    if driver.delete(id):
        response.status = 204
    response.status = 404

bottle.debug(True)
bottle.run(host='localhost', port=8080, reloader=True)
