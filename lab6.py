from turtle import *
import random
import math
import turtle

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

Mimi = Ball(30, "pink", 10)
Bob = Ball(40, "black", 2)

def check_collision(Mimi, Bob):
	Mimi_x, Mimi_y = Mimi.pos()
	Bob_x, Bob_y = Bob.pos()

	d = math.sqrt(math.pow(Mimi_x-Bob_x, 2) + math.pow(Mimi_y-Bob_y, 2))
	if Mimi.radius + Bob.radius >= d:
		print("collision")
	else:
		print("no collision")

check_collision(Mimi,Bob)

turtle.mainloop()

