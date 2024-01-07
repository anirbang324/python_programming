# Python program to draw
# Spiral Helix Pattern
# using Turtle Programming
import turtle
import random
loadWindow = turtle.Screen()
colours=["red","green","blue","orange","SeaGreen"]
turtle.speed(10)
for i in range(100):
	turtle.color(random.choice(colours))
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.right(i)

turtle.exitonclick()
