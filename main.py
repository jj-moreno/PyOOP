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

    def randmove(self, new_point):
        new_x = new_point.x
        new_y = new_point.y
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

    def getdistance(self, new_loc):
        distance = Segment(self.start_loc, new_loc).length()
        return distance

    def __getattribute__(self, start_loc):
        return object.__getattribute__(self, start_loc)


class Trial(object):
    def __init__(self, alloted_time, start_point=Point(0, 0)):
        self.drunk = Drunk(start_point)
        self.field = Field(self.drunk)
        self.alloted_time = alloted_time
        self.distances = []

    def performtrial(self):
        current_time = 0
        while current_time < self.alloted_time:
            self.drunk.randmove(self.drunk.drunk_loc)
            drunk_loc = self.drunk.drunk_loc
            distance_traveled = self.field.getdistance(drunk_loc)
            self.distances.append(distance_traveled)
            current_time += 1

    def printresult(self):
        print(self.distances)


if __name__ == '__main__':
    time_in_secs = 5
    trial = Trial(time_in_secs)
    trial.performtrial()
    trial.printresult()
