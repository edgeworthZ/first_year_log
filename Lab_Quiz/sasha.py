import turtle
import math

alex = turtle.Turtle()
sc = turtle.Screen()

def tri(d):
    for j in range(3):
        alex.forward(d)
        alex.right(120)

def window(d):
    for i in range(4):
        for j in range(4):
            alex.forward(d)
            alex.right(90)
        alex.right(90)

def star(d):
    tri(d)
    alex.forward(d)
    alex.right(90)
    alex.penup()
    alex.forward(d/math.sqrt(3))
    alex.right(90)
    alex.pendown()
    tri(d)

def triangle(d):
    alex.forward(d)
    alex.left(135)
    alex.forward(math.sqrt(2*d**2))
    alex.left(135)
    alex.forward(d)

pic = input('Input picture name: ')
d = int(input('Input d: '))
if pic == 'window':
    window(d)
elif pic == 'six-point star':
    star(d)
elif pic == 'right triangle':
    triangle(d)
sc.exitonclick()
