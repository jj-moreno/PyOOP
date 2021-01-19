import math
import random


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, x, y):
        return object.__setattr__(self, x, y)

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


class Field(object):
    def __init__(self, drunk):
        self.start_location = drunk.location

    def __getattribute__(self, start_location):
        return object.__getattribute__(self, start_location)


class Trial(object):
    def __init__(self, alloted_time, start_point=Point(0, 0)):
        self.alloted_time = alloted_time
        self.drunk = Drunk(start_point, 1)
        self.field = Field(self.drunk)
        self.distances = []

    def getdistance(self):
        segment = Segment(self.field.start_location, self.drunk.location)
        return segment.length()

    def performtrial(self):
        current_time = 0
        while current_time < self.alloted_time:
            self.drunk.randmove()
            distance_traveled = self.getdistance()
            self.distances.append(distance_traveled)
            current_time += 1

    def printresult(self):
        print(self.distances)


if __name__ == '__main__':
    time_in_secs = 5
    trial = Trial(time_in_secs)
    trial.performtrial()
    trial.printresult()
