import ConfigParser
import sys
import uuid

from cassandra import cluster

import base_driver
import model


class CassandraDriver(base_driver.BaseDriver):

    def __init__(self):
        config = ConfigParser.ConfigParser()
        host = config.get('cassandra', 'host')
        db = cluster.Cluster([host])
        self._session = db.connect('todos')

    def get(self, id):
        _id = uuid.UUID(id)
        query = 'SELECT id, title, description FROM todos WHERE id = %s'
        results = self._session.execute(query, (_id,))
        for (id, title, description) in results:
            return model.ToDo(title, description, id)
        return None

    def get_all(self):
        todos = []

        query = 'SELECT id, title, description FROM todos'
        results = self._session.execute(query)
        for (id, title, description) in results:
            todos.append(model.ToDo(title, description, id))
        return todos

    def insert(self, todo):
        new_id = uuid.uuid4()
        query = 'INSERT INTO todos (id, title, description)' \
            'VALUES (%s, %s, %s)'
        self._session.execute(query, (new_id, todo.title, todo.description))

    def delete(self, id):
        _id = uuid.UUID(id)
        query = 'DELETE FROM todos WHERE id = %s'
        self._session.execute(query, (_id,))
