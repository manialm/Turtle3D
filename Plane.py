# the plane always passes through the camera point
class Plane:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __iter__(self):
        return iter((self.a, self.b, self.c))

    def __repr__(self):
        return f'Plane({self.a}, {self.b}, {self.c})'
