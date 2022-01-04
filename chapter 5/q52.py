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
s="\u03c0"
cx=1
cxx=-3
turtle.goto(-175,50)
for x in range(-175,176):
    y=50*math.sin((x/100)*2*math.pi)
    turtle.pendown()
    turtle.goto(x,y)
    if int(y)==0:
        if x>0:
            turtle.write(str(cx)+s)
            cx+=1
        if x<0:
            turtle.write("-"+str(cxx)+s)
            cxx+=1

turtle.penup()
turtle.done()


