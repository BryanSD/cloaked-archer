import abc


class BaseDriver(object):

    @abc.abstractmethod
    def get(self, id):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_all(self):
        """Returns a list of model.ToDo instances"""
        raise NotImplementedError()

    @abc.abstractmethod
    def insert(self, todo):
        """Inserts a model.ToDo into the database.

        model.ToDo.id will be ignored and set by the database.
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, id):
        """Return True if deleted, False if not found"""
        raise NotImplementedError()
