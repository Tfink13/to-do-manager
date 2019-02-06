import datetime
import time
from datetime import date

# i need a timestamp i know i import but i dont undertsand how it works inside the class
class Item(object):
    def __init__(self):
        self.date = date.datetime.today()
        self.lsit_item = []
        self.completed = False
