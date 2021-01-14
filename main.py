import math
import random


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


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Drunk(object):
    possibilites = ['N', 'S', 'E', 'W']

    def __init__(self, start_loc):
        self.start_loc = start_loc

    def rand_move(self, point):
        x = point.x
        y = point.y
        randmove = random.choice(self.possibilites)
        if randmove == 'N':
            return Point(x, y + 1)
        elif randmove == 'S':
            return Point(x, y - 1)
        elif randmove == 'E':
            return Point(x + 1, y)
        else:  # must be W
            return Point(x - 1, y)

    def __getattribute__(self, start_loc):
        return object.__getattribute__(self, start_loc)


class Field(object):
    distances = []

    def __init__(self, drunk):
        self.drunk = drunk
        self.start_loc = drunk.start_loc
        self.curr_loc = self.start_loc

    def calc_dist_from_start(self, curr_loc):
        self.curr_loc = curr_loc
        distancetravel = Segment(self.start_loc, self.curr_loc).length()
        self.distances.append(distancetravel)

    def __getattribute__(self, distances):
        return object.__getattribute__(self, distances)


def perform_trial(time, num_trials):
    start_location = Point(0, 0)
    drunk = Drunk(start_location)
    field = Field(drunk)
    current_location = drunk.rand_move(start_location)
    for t in range(time):
        field.calc_dist_from_start(current_location)
        current_location = drunk.rand_move(field.curr_loc)
    print(field.distances)


if __name__ == '__main__':
    # point1 = Point(0, 6)
    # point2 = Point(2, 8)
    # segment1 = Segment(point1, point2)
    # print(segment1)
    # print(segment1.length())
    perform_trial(5, 3)
