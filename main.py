import random
import turtle


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def draw_ten_dots():
    for i in range(10):
        bob.dot(20, random_color())
        bob.forward(50)


def back_to_next_position():
    bob.setheading(90)
    bob.forward(50)
    bob.setheading(180)
    bob.forward(500)
    bob.setheading(0)


bob = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()
bob.hideturtle()
bob.penup()
bob.speed(0)
bob.goto(x=-250, y=-250)

for i in range(10):
    draw_ten_dots()
    back_to_next_position()
screen.exitonclick()
