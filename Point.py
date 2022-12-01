class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, x, y):
        return object.__setattr__(self, x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"
