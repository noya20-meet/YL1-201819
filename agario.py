import turtle
import time
import random 
import math
from Ball import*
turtle.setup(1900, 1080)
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
global running
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
#Part 1#
my_ball = Ball(0, 0, 8, 5, 40, "light pink")
number_of_balls = 7
minimum_ball_radius = 15
maximum_ball_radius = 110
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
global score
score = 0

#Part 2#
BALLS = []
for i in range (number_of_balls):
	x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	r = random.randint(minimum_ball_radius, maximum_ball_radius)
	color = (random.random(), random.random(), random.random())
	new_ball = Ball(x, y, dx, dy, r, color)
	BALLS.append(new_ball)

def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width, screen_height)
#Part 3#
def collide (ball_a, ball_b):
	if ball_a == ball_b :
		return False
	d = math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(),2) + math.pow(ball_a.ycor() - ball_b.ycor(),2))
	if d <= ball_a.r + ball_b.r:
		return True
	else:
		return False
#Part 4#
def called_all_balls_collision():
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a in all_balls:
		for ball_b in all_balls:
			if collide(ball_a, ball_b):
				global score
				global running
				r1 = ball_a.r
				r2 = ball_b.r 
				x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
				y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
				dx = random.randint(minimum_ball_dx, maximum_ball_dx)
				dy = random.randint(minimum_ball_dy, maximum_ball_dy)
				r = random.randint(minimum_ball_radius, maximum_ball_radius)
				color = (random.random(), random.random(), random.random())
				if (r1>r2):
					ball_b.new_ball(x, y, dx, dy, r, color)
					ball_a.r = ball_a.r + 5
					ball_a.shapesize(ball_a.r/10)
					if my_ball == ball_b:
						running = False
					if my_ball == ball_a:
						running = True
						score = score + 10


#Part 5#
def movearound():
	x = turtle.getcanvas().winfo_pointerx() - screen_width
	y = screen_height - turtle.getcanvas().winfo_pointery()

	my_ball.goto(x,y)
#part 6 + score#
turtle.ht()
for num in range(1,4):
	for size in range(100):
		turtle.clear()
		turtle.write(num, font=("Lato Heavy", size, "normal"))
		time.sleep(.01)

turtle.goto(0,screen_height-200)

while running == True:
	turtle.clear()
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	movearound()
	move_all_balls()
	called_all_balls_collision()
	turtle.update()
	turtle.write("score: " + str(score), font=("Lato Heavy", 50, "normal"))
	time.sleep(.05)

turtle.mainloop() 