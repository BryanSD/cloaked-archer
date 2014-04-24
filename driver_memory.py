import base_driver


class MemoryDriver(base_driver.BaseDriver):

    def __init__(self):
        self._id_counter = 0
        self._todos = list()

    def get(self, id):
        for todo in self._todos:
            if todo.id == id:
                return todo
        return None

    def get_all(self):
        return self._todos

    def insert(self, todo):
        todo.id = self._id_counter
        self._id_counter += 1
        self._todos.append(todo)

    def delete(self, id):
        for todo in self._todos:
            if todo.id == id:
                self._todos.remove(todo)
                return True
        return False
