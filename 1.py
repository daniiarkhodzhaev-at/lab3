#!/usr/bin/python3

import turtle
import random

STEP = 5

def rw_step0() -> None:
    turtle.forward(STEP)
    turtle.left(random.randint(0, 360))

def rw_step1() -> None:
    x, y = turtle.pos()
    dirr = random.randint(0,3)
    if (dirr == 0):
        x += STEP
    elif (dirr == 1):
        x -= STEP
    elif (dirr == 2):
        y += STEP
    elif (dirr == 3):
        y -= STEP
    else:
        raise ValueError("Incorrect value of dirr")
    turtle.goto(x,y)

rw_step = [rw_step0, rw_step1]

def main() -> int:
    turtle.shape("turtle")
    turtle.speed(0)
    rw_type = input("Choose type of random walk:\n(0) all directions,\n(1) discrete (only 4 directions)\n")
    while (not rw_type in ["0", "1"]):
        rw_type = input("Incorrect input, answer should be \"0\" or \"1\". Try again.\n")
    rw_type = int(rw_type)
    while (True):
        rw_step[rw_type]()
    return 0

if (__name__ == "__main__"):
    main()
