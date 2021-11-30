from turtle import *
from Plane import *
from transform import *
from math import sin, cos

# setup
shape = 'octahedron'
SCALE = 100
dt = 0.002
pu()
speed('fastest')
hideturtle()
bgcolor('black')
pencolor('aqua')
tracer(0)

vertices = []
with open(f'shapes/{shape}_vertices.txt') as f:
    for line in f:
        x, y, z = [float(i) for i in line.split()]
        vertices.append(Vector(x, y, z))

t = 0
while True:
    camera_pos = Vector(3 * cos(t), 3 * sin(t), 0)
    camera_plane = Plane(3 * cos(t), 3 * sin(t), sin(t))

    new_vertices = [transform(vertex, camera_pos, camera_plane) for vertex in vertices]

    with open(f'shapes/{shape}_edges.txt', 'r') as f:
        for line in f:
            i, j = map(int, line.split())

            x, y = new_vertices[i]
            goto(x * SCALE, y * SCALE)
            pd()

            x, y = new_vertices[j]
            goto(x * SCALE, y * SCALE)
            pu()

    update()

    t += dt
    clear()
