# import math


class Segment(object):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __str__(self):
        return f"start_point: ({self.start_point.x}, { self.start_point.y})\n" \
               f"end_point: ({self.end_point.x}, { self.end_point.y})\n"


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    point1 = Point(0, 6)
    point2 = Point(2, 8)
    segment1 = Segment(point1, point2)
    print(segment1)
