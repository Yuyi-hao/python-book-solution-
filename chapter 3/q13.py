import math
import turtle
h=math.sqrt(3)
a=200/h
turtle.penup()
turtle.goto(a,-100)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(a,360,6)
turtle.end_fill()
turtle.penup()
turtle.goto(80,-15)
turtle.pendown()
turtle.color("white")
turtle.write("stop",font = ("Times", 30, "bold"))
turtle.hideturtle()
turtle.done()

