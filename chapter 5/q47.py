import turtle 
import random
width = 120
height = 100
turtle.penup()
turtle.goto(-width/2,-height/2)
turtle.pendown()
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)

for i in range(1,11,1):
    x = random.randint(-width/2+5,width/2-5)
    y = random.randint(-height/2+5,height/2-5)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(6,'red')
turtle.done()