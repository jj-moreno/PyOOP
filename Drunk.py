import random
from Point import Point


class Drunk(object):
    possibilites = ['N', 'S', 'E', 'W']

    def __init__(self, start_point, step_length):
        self.location = start_point
        self.step_length = step_length

    def randmove(self):
        new_x = self.location.x
        new_y = self.location.y
        rand_move = random.choice(self.possibilites)
        if rand_move == self.possibilites[0]:
            new_y = new_y + self.step_length
        elif rand_move == self.possibilites[1]:
            new_y = new_y - self.step_length
        elif rand_move == self.possibilites[2]:
            new_x = new_x + self.step_length
        else:  # must be last possibility, self.possibilites[3]
            new_x = new_x - self.step_length
        self.location = Point(new_x, new_y)

    def __getattribute__(self, location):
        return object.__getattribute__(self, location)
