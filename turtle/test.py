#we are going to draw triangle,square,pentagon,hexagon,heptagon,octagon,nonagon,decagon
import turtle
import turtle as t
import random
t1=t.Turtle()
t1.speed(5)
colours=["red","green","blue","orange","SeaGreen","violet","indigo","teal","lime","maroon"]
def draw_shape(num_sides):
	angle = 360/ num_sides
	for _ in range(num_sides):
		t1.forward(100)
		t1.right(angle)
for shape_side_n in range(3,17):
	t1.color(random.choice(colours))
	draw_shape(shape_side_n)
turtle.done()