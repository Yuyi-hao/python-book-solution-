import turtle
radius = 100
for i in range(1,11,1):
    turtle.penup()
    turtle.goto(0,-radius)
    turtle.pendown()
    turtle.circle(radius)
    radius += 20
turtle.done()