import turtle

radius = eval(input("Enter the radius : "))

turtle.penup()
turtle.goto(radius,0)
turtle.pendown()
turtle.circle(radius,360,6)
turtle.penup()
turtle.goto(-radius,0)
turtle.pendown()
turtle.circle(radius,360,6)
turtle.penup()
turtle.goto(-radius,-2*radius)
turtle.pendown()
turtle.circle(radius,360,6)
turtle.penup()
turtle.goto(radius,-2*radius)
turtle.pendown()
turtle.circle(radius,360,6)
turtle.done()