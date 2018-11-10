"""
    Specify the kinds of objects to use a prototypical instance, and create
    new objects by copying this prototype.
    
    Usecase: When the creation of the an object is costly, consider a class which 
    requires a file or a database and needs this for initialization.
    For example the builder pattern is great for building a car in our example
    but what if you want to build thousands of car. The solution is that we make
    car a prototype class.
"""

from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        obj = deepcopy(self)
        obj.move(move_x, move_y)

        return obj
