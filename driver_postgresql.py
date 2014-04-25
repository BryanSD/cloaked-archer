import sys
import uuid

import psycopg2

import base_driver
from model import ToDo


class PostgreSQLDriver(base_driver.BaseDriver):

    def __init__(self):
        db = sys.argv[2]
        user = sys.argv[3]
        password = sys.argv[4]
        self.conn = psycopg2.connect(
            "dbname=%s user=%s password=%s" % (db, user, password)
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
            (uuid.uuid4(), todo.title, todo.description)
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
