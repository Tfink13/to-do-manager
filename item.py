



# i need a timestamp i know i import but i dont undertsand how it works inside the class
class Item(object):
    def __init__(self, task = None, completed = False, date = None):
        list = []
        self.task = task
        self.completed = completed
        self.date = date.datetime.now()
