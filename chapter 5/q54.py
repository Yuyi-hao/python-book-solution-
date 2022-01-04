import turtle
import math
turtle.speed(10) 
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.forward(400)
turtle.penup()
turtle.goto(190,5)
turtle.pendown()
turtle.goto(200,0)
turtle.goto(190,-5)
turtle.penup()
turtle.goto(200,15)
turtle.write('x')
turtle.penup()
turtle.left(90)
turtle.goto(0,-100)
turtle.pendown()
turtle.forward(200)
turtle.penup()
turtle.goto(-5,90)
turtle.pendown()
turtle.goto(0,100)
turtle.goto(5,90)
turtle.penup()
turtle.goto(15,100)
turtle.write('y')

scaleFactor = 0.01
left = -100
right = 100
x = left
turtle.penup()
turtle.goto(x, scaleFactor * x * x)
turtle.pendown()
for x in range(left, right + 1,1):
    turtle.goto(x, scaleFactor * x * x)

turtle.penup()
turtle.done()
