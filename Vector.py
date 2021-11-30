from math import sqrt

# a vector is also a point
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalize(self):
        return self / abs(self)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, r):
        return Vector(self.x * r, self.y * r, self.z * r)

    def __truediv__(self, r):
        return Vector(self.x / r, self.y / r, self.z / r)

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'
