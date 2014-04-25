import ConfigParser
import sys
import uuid

import psycopg2

import base_driver
from model import ToDo


class PostgreSQLDriver(base_driver.BaseDriver):

    def __init__(self):
        config = ConfigParser.ConfigParser()
        db =       config.get('postgresql', 'database')
        user =     config.get('postgresql', 'user')
        password = config.get('postgresql', 'password')
        host =     config.get('postgresql', 'host')
        port =     config.get('postgresql', 'port')

        self.conn = psycopg2.connect(
            dbname=db,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def get(self, id):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM todos WHERE id = %s;",
            (id,)
        )
        (row_id, title, descr) = cursor.fetchone()
        cursor.close()
        return ToDo(title, descr, row_id)

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, description FROM todos;")
        raw_results = cursor.fetchall()
        print raw_results
        result = [ToDo(title, descr, row_id) for (row_id, title, descr) in raw_results]
        print result
        cursor.close()
        return result

    def insert(self, todo):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO todos (id, title, description) VALUES (%s, %s, %s);",
            (uuid.uuid4().hex, todo.title, todo.description)
        )
        self.conn.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM todos WHERE id = %s;",
            (id,)
        )
        self.conn.commit()
        result = cursor.rowcount > 0
        cursor.close()
        return result
