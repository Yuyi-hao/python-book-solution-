#Enter the first point p1 (x1,y1):10 50
#put a space in between 10 and 50
#if u put a " , " in between it treats it like a single string
import math 
import turtle
x1,y1 = map(float,input("Enter the first point p1 (x1,y1):").split())
x2,y2 = map(float,input("Enter the second point p2 (x2,y2):").split())
x3,y3 = map(float,input("Enter the third point p3 (x3,y3):").split())
a=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
b=math.sqrt(pow(x1-x3,2)+pow(y1-y3,2))
c=math.sqrt(pow(x3-x2,2)+pow(y3-y2,2))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("("+str(x1)+","+str(y1)+")")
turtle.goto(x2,y2)
turtle.write("("+str(x2)+","+str(y2)+")")
turtle.goto(x3,y3)
turtle.write("("+str(x3)+","+str(y3)+")")
turtle.goto(x1,y1)
turtle.penup()
turtle.goto(-75,-75)
turtle.pendown()
turtle.write("The area of triangle is:"+str(area),move=True,font=("Verdana",15,"normal"))
turtle.done()
print(area)