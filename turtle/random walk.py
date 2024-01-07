import turtle as t
import random
t1= t.Turtle()
colours=["red","green","blue","orange","yellow","wheat","SlateGray","SeaGreen"]
directions=[0,90,105,270]
t1.pensize(15)
t1.speed(10)  #speed should be in between 0 to 10
for _ in range(1000):
	t1.color(random.choice(colours))
	t1.forward(30)
	t1.setheading(random.choice(directions))
	t1.backward(10)#to pick a random directions
