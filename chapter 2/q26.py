import turtle
import math 
x,y,radius = eval(input("Enter the coordinates of center and radius (x,y,radius) : "))

area = radius*radius*math.pi

text = '{:.2f}'.format(area)

turtle.penup()
turtle.goto(x,y-radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.write(text)
turtle.done()

