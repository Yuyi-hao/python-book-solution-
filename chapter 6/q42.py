import turtle
import listing14
import math
turtle.speed(10) 
listing14.drawLine(-200,0,200,0)
listing14.drawLine(190,5,200,0)
listing14.drawLine(200,0,190,-5)
listing14.writeText('X',200,5)
listing14.drawLine(0,-100,0,100)
listing14.drawLine(-5,90,0,100)
listing14.drawLine(0,100,5,90)
listing14.writeText('Y',15,100)
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


