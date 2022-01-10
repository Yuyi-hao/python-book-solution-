import turtle
import listing14
turtle.speed(10)
# making x axis  
listing14.drawLine(-200,0,200,0)
listing14.drawLine(190,5,200,0)
listing14.drawLine(200,0,190,-5)
listing14.writeText('X',200,5)
listing14.drawLine(0,-100,0,100)
listing14.drawLine(-5,90,0,100)
listing14.drawLine(0,100,5,90)
listing14.writeText('Y',15,100)
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
