# Python program to draw hexagon
# using Turtle Programming
import turtle
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
turtle.speed(0.1)  # 0  to 10
angle = 60
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
