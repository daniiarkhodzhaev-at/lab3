#!/usr/bin/python3

import turtle
import random

dt = 0.01
vx = 10
vy = 0
ax = 0
ay = -10

# This is not exactly energy, it's divided by mass (because it's proportional to it)
def get_energy() -> float:
    return (turtle.dot_x ** 2 + turtle.dot_y ** 2) / 2 - turtle.pos()[1] * ay

# Just double integration
def dull_simulate() -> int:
    x, y = turtle.pos()
    x += turtle.dot_x * dt
    y += turtle.dot_y * dt
    turtle.dot_x += ax * dt
    turtle.dot_y += ay * dt
    if (y <= 0 or y >= 550):
        turtle.dot_y *= -1
    if (x <= -500 or x >= 500):
        turtle.dot_x *= -1
    turtle.goto(x, y)
    return 0

# Now energy conserves, however, there are some problems with impulse
def better_simulate() -> int:
    dull_simulate()
    kin_energy = turtle.energy
    kin_energy += turtle.pos()[1] * ay
    kin_energy *= 2 # this is not exactly kinetic energy, but it's proportional to it
    alpha = (kin_energy / (turtle.dot_x ** 2 + turtle.dot_y ** 2)) ** 0.5
    # scaling velocity vector, so full energy conserves
    turtle.dot_x *= alpha
    turtle.dot_y *= alpha
    return 0

def main() -> int:
    turtle.shape("circle")
    turtle.speed(0)
    turtle.dot_x = vx
    turtle.dot_y = vy
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.energy = get_energy()
    while (not better_simulate()):
        pass
    return 0

if (__name__ == "__main__"):
    main()
