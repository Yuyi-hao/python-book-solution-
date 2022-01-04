import turtle
turtle.speed(10)
turtle.penup()
turtle.goto(-180,-180)
turtle.pendown()
for s in range(4):
    turtle.forward(360)
    turtle.left(90)
turtle.penup()
turtle.goto(-180,180)
for x in range(-180,180,10):
    turtle.penup()
    turtle.goto(-180,x)
    turtle.pendown()
    turtle.forward(360)
turtle.penup()
turtle.left(90)
turtle.goto(-180,-180)
for y in range(-180,180,10):
    turtle.penup()
    turtle.goto(y,-180)
    turtle.pendown()
    turtle.forward(360)

turtle.done()

