from turtle import *
from Plane import *
from transform import *
from math import sin, cos

# setup
shape = 'torus'
SCALE = 300
dt = 0.02
pu()
speed('fastest')
hideturtle()
bgcolor('black')
pencolor('red')
tracer(0)

vertices = []
with open(f'shapes/{shape}_vertices.txt') as f:
    for line in f:
        x, y, z = [float(i) for i in line.split()]
        vertices.append(Vector(x, y, z))

t = 0
while True:
    camera_pos = Vector(3 * cos(t), 3 * sin(t), 2*sin(t)) * 0.5
    camera_plane = Plane(3 * cos(t), 3 * sin(t), 2*sin(t))

    new_vertices = [transform_with_perspective(vertex, camera_pos, camera_plane) for vertex in vertices]

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
