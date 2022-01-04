import turtle
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
y=100
for i in range(0,12):
    for j in range(1,i):
        turtle.write(str(j))
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
    turtle.penup()
    turtle.goto(-100,y)
    y=y-20
turtle.done()