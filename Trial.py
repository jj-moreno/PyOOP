from Drunk import Drunk
from Field import Field
from Point import Point
from Segment import Segment


class Trial(object):
    def __init__(self, alloted_time, start_point=Point(0, 0)):
        self.alloted_time = alloted_time
        self.drunk = Drunk(start_point, 1)
        self.field = Field(self.drunk)
        self.distances = [0]

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
