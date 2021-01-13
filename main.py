import math


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

    def rand_move(self, coordinates):
        # TODO:
        return (0, 0)

    def __getattribute__(self, start_loc):
        return object.__getattribute__(self, start_loc)


class Field(object):

    def __init__(self, drunk):
        self.drunk = drunk
        self.start_loc = drunk.start_loc
        self.curr_loc = self.start_loc


def perform_trial(time, num_trials):
    print(time, num_trials)


if __name__ == '__main__':
    # point1 = Point(0, 6)
    # point2 = Point(2, 8)
    # segment1 = Segment(point1, point2)
    # print(segment1)
    # print(segment1.length())
    start_location = Point(0, 0)
    drunk = Drunk(start_location)
    field = Field(drunk)
    perform_trial(1000, 3)
