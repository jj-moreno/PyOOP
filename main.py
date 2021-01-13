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


class Drunk(object):
    possibilites = ['N', 'S', 'E', 'W']

    def rand_move(self, coordinates):
        # TODO:
        return (0, 0)


class Field(object):
    start_loc = (0, 0)
    curr_loc = (0, 0)

    def __init__(self, drunk):
        self.drunk = drunk


def perform_trial(time, num_trials):
    print(time, num_trials)


if __name__ == '__main__':
    # point1 = Point(0, 6)
    # point2 = Point(2, 8)
    # segment1 = Segment(point1, point2)
    # print(segment1)
    # print(segment1.length())
    perform_trial(1000, 3)
