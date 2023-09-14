from Vector import *
from solve import *


def distance_from_plane(point, plane):
    x, y, z = point
    a, b, c = plane

    t = -(a*x + b*y + c*z) / (a**2 + b**2 + c**2)
    
    return abs(t * abs(Vector(a, b, c)))


def project(point, plane):
    x, y, z = point
    a, b, c = plane

    t = -(a*x + b*y + c*z) / (a**2 + b**2 + c**2)

    return Vector(x + a*t, y + b*t, z + c*t)


def find_basis(plane, point=Vector(0, 0, 0)):
    a, b, c = plane
    x, y, z = point

    d = -(a * x + b * y + c * z)
    b1 = Vector(d / a - b, a, 0).normalize()
    x, y = solve(a, b, d - c, -b, a, 0)
    b2 = Vector(x, y, 1).normalize()
    return b1, b2


# from 3D to 2D
def transform(point, origin, plane):
    point -= origin
    proj = project(point, plane)
    x, y, z = proj
    b1, b2 = find_basis(plane)
    u, v = solve(b1.x, b2.x, x, b1.y, b2.y, y)
    # check:  z == b1.z * u + b2.z * v
    return u, v

def transform_with_perspective(point, origin, plane):
    point -= origin
    proj = project(point, plane)

    distance = distance_from_plane(point, plane)

    x, y, z = proj
    b1, b2 = find_basis(plane)
    u, v = solve(b1.x, b2.x, x, b1.y, b2.y, y)
    # check:  z == b1.z * u + b2.z * v

    return u / distance, v / distance

