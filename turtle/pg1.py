# Python program to draw star
# using Turtle Programming
import turtle
star = turtle.Turtle()
star.setpos(60,30)
#star.pos(60.00,30.00)
star.color("blue")
star.shape("triangle")  #turtle
angle = 90
#star.right(100)
star.speed(2)  # 1 to 10
#star.forward(100)  #right 90 degree
for i in range(4):  #9 times
    star.right(144)
    star.forward(100)
turtle.done()
