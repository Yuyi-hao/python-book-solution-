import turtle
turtle.penup()
turtle.speed(10)
turtle.goto(-250,250)
turtle.pendown()
turtle.write("Multiplication Table", font=("ds-digital", 40, "bold"))
turtle.penup() 
turtle.goto(-200,210)
turtle.color("red")
for i in range(1,10):
    turtle.write(str(i), font=("arial", 20))
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
turtle.penup()
turtle.goto(-350,180)
turtle.pendown()
turtle.write("----------------------------------------------------------------------------", font=("ds-digtal", 20, "bold"))
turtle.penup()
turtle.goto(-340,150)
z=150
turtle.pendown()
for j in range (1,10):
    turtle.write(str(j)+"  |", font=("arial", 20 ))
    turtle.penup()
    turtle.forward(140)
    for k in range(1,10):
        turtle.write(str(j*k), font=("arial", 20))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    z=z-50
    turtle.penup()
    turtle.goto(-340,z)
    
turtle.done()