#!/usr/bin/python3

u = 25
step = 30

DIGITS = [((0,0), (u,0), (u,2*u), (0,2*u), (0,0)),
          ((0,u), (u,2*u), (u,0)),
          ((u,0), (0,0), (u,u), (u,2*u), (0,2*u)),
          ((0,0), (u,u), (0,u), (u,2*u), (0,2*u)),
          ((u,0), (u,2*u), (u,u), (0,u), (0,2*u)),
          ((0,0), (u,0), (u,u), (0,u), (0,2*u), (u,2*u)),
          ((0,u), (u,u), (u,0), (0,0), (0,u), (u,2*u)),
          ((0,0), (0,u), (u,2*u), (0,2*u)),
          ((0,u), (u,u), (u,0), (0,0), (0,2*u), (u,2*u), (u,u)),
          ((0,0), (u,u), (u,2*u), (0,2*u), (0,u), (u,u))]

import turtle

def draw_digit(N: int) -> None:
    assert 0 <= N <= 9
    _x, _y = turtle.pos()
    turtle.penup()
    for point in DIGITS[N]:
        x, y = point
        x += _x
        y += _y
        turtle.goto(x, y)
        turtle.pendown()
    turtle.penup()
    turtle.goto(_x + step, _y)

def test() -> None:
    for i in range(10):
        draw_digit(i)

def main() -> int:
    turtle.shape("turtle")
    turtle.speed(0)
    # test()
    for i in [1, 4, 1, 7, 0, 0]:
        draw_digit(i)
    turtle.mainloop()
    return 0

if (__name__ == "__main__"):
    main()
