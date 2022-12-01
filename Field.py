class Field(object):
    def __init__(self, drunk):
        self.start_location = drunk.location

    def __getattribute__(self, start_location):
        return object.__getattribute__(self, start_location)
