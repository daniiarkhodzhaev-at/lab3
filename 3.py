#!/usr/bin/python3

import json
import turtle

u = 25
step = 30

digits = []

def load_digits() -> None:
    global digits
    digit_file = open("post_digits.json", 'r')
    digits = json.load(digit_file)
    digit_file.close()

def draw_digit(N: int) -> None:
    assert 0 <= N <= 9
    _x, _y = turtle.pos()
    turtle.penup()
    for point in digits[str(N)]:
        x, y = point
        x *= u
        y *= u
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
    load_digits()
    turtle.shape("turtle")
    turtle.speed(0)
    # test()
    for i in [1, 4, 1, 7, 0, 0]:
        draw_digit(i)
    turtle.mainloop()
    return 0

if (__name__ == "__main__"):
    main()
