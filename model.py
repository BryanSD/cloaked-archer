class ToDo(object):

    def __init__(self, title, description, id=None):
        self.id = id
        self._title = title
        self._description = description

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description
