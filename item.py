import datetime
import time
from datetime import date



# i need a timestamp i know i import but i dont undertsand how it works inside the class
class Item(object):
    def __init__(self, task = None, completed = False, date = None):
        list = []
        self.task = task
        self.completed = completed
        self.date = date.datetime.now()



task1 = Item()
task1.task('Mop the floor')
task1.completed(False)
