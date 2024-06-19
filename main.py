# First JOC Code
# By John Schlautman
# 6/19/24

import turtle
import random
# def triangle(size, color):
#  turtle.color(color)
#  for i in range(3):
#    turtle.forward(size)
#    turtle.left(120)


turtles = []
colors = ["green", "blue", "red", "black", "orange", "purple", "brown", "pink"]

for i in range(len(colors)):
  t = turtle.Turtle()
  t.speed(0)
  t.shape("turtle")
  turtles.append(t)
  t.color(colors[i])
  t.right(i*60)
  t.forward(20)
  t.penup()
  
ANGLE = 50
MAX_DISTANCE = 10
ITERATIONS = 100
for i in range(ITERATIONS):
    for t in turtles:
      t.right(random.randint(-1*ANGLE,ANGLE))
      t.forward(random.randint(1, MAX_DISTANCE))
