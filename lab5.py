from turtle import
import turtle
import random
colormode(225)
class Square(Turtle):
	def __init__ (self, size):
		Turtle.__init__(self)
		self.shape("square")
		self.size = size
		self.shapesize(size*size)
	def random_color(self):
		r = random.randint(0,255) 
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color
