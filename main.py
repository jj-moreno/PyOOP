import math
import random


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Segment(object):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f"start_point: ({self.start_point.x}, {self.start_point.y})\n" \
               f"end_point: ({self.end_point.x}, {self.end_point.y})\n"

    def length(self):
        return math.sqrt(abs(self.end_point.x - self.start_point.x) ** 2
                         + abs(self.end_point.y - self.start_point.y) ** 2)


class Drunk(object):

    def __init__(self, start_point):
        self.drunk_loc = start_point
        self.possibilites = ['N', 'S', 'E', 'W']

    def randmove(self, point):
        new_x = point.x
        new_y = point.y
        rand_move = random.choice(self.possibilites)
        if rand_move == self.possibilites[0]:
            new_y = new_y + 1
        elif rand_move == self.possibilites[1]:
            new_y = new_y - 1
        elif rand_move == self.possibilites[2]:
            new_x = new_x + 1
        else:  # must be last possibility, self.possibilites[3]
            new_x = new_x - 1
        self.drunk_loc = Point(new_x, new_y)

    def __getattribute__(self, drunk_loc):
        return object.__getattribute__(self, drunk_loc)


class Field(object):

    def __init__(self, drunk):
        self.start_loc = drunk.drunk_loc

    def getdistance(self, start_loc, new_loc):
        distance = Segment(start_loc, new_loc).length()
        return distance

    def __getattribute__(self, start_loc):
        return object.__getattribute__(self, start_loc)


class Trial(object):

    def __init__(self, time, start_point=Point(0, 0)):
        self.drunk = Drunk(start_point)
        self.field = Field(self.drunk)
        self.time = time
        self.distances = []

    def perform_trial(self):
        current_time = 0
        start_loc = self.field.start_loc
        while current_time < self.time:
            self.drunk.randmove(self.drunk.drunk_loc)
            drunk_loc = self.drunk.drunk_loc
            distancetravel = self.field.getdistance(start_loc, drunk_loc)
            self.distances.append(distancetravel)
            current_time += 1

    def print_result(self):
        print(self.distances)


if __name__ == '__main__':
    trial = Trial(5)
    trial.perform_trial()
    trial.print_result()
