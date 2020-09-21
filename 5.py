#!/usr/bin/python3

import turtle
import random

llcorner = (-200, -200)
urcorner = (200, 200)

dt = 0.1
nspeed = 2

def getRandomCoords() -> tuple:
    return (random.randrange(llcorner[0], urcorner[0]), random.randrange(llcorner[1], urcorner[1]))

def f(x_0: float, y_0: float, x: float, y: float) -> tuple:
    return (0, 0)

def main() -> int:
    turtle.ht()
    a = []
    for i in range(20):
        a.append(turtle.Turtle())
        a[-1].shape("circle")
        a[-1].speed(0)
        a[-1].penup()
        a[-1].goto(*getRandomCoords())
        a[-1].dotx = (random.random() * 2 - 1) * nspeed
        a[-1].doty = (random.random() * 2 - 1) * nspeed
    while (True):
        for i in a:
            pass
            # i.ht()
        for i in a:
            pos = i.pos()
            i.goto(pos[0] + i.dotx * dt, pos[1] + i.doty)
        for i in a:
            for j in a:
                argsi = i.pos()
                argsj = j.pos()
                args = (argsi[0], argsi[1], argsj[0], argsj[1])
                F = f(*args)
                i.dotx += F[0] * dt
                i.doty += F[1] * dt
                j.dotx += -F[0] * dt
                j.doty += -F[1] * dt
        for i in a:
            p = i.pos()
            if (p[0] < llcorner[0] or p[0] > urcorner[0]):
                i.dotx *= -1
            if (p[1] < llcorner[1] or p[1] > urcorner[1]):
                i.doty *= -1
        for i in a:
            pass
            # i.st()
    return 0

if (__name__ == "__main__"):
    main()
