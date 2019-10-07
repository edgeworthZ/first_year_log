import turtle
import math

alex = turtle.Turtle()
sc = turtle.Screen()
sc.setworldcoordinates(0,-1,360,1)
for x in range(360):
  y = math.sin(math.radians(x))
  alex.goto(x,y)
sc.exitonclick()
