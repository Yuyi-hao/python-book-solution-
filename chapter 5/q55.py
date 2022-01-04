import turtle
turtle.bgcolor("blue")
turtle.penup()
turtle.speed(10)
turtle.goto(-130,240)
turtle.color("red")
turtle.write("CHESSBOARD", font=("ds-digital",40,"bold"))
turtle.penup()
turtle.color("black")
#turtle.goto(-24,240)
turtle.goto(-200,-200)
turtle.pendown()
for s in range(4):
                turtle.forward(400)
                turtle.left(90)
turtle.penup()
turtle.goto(-200,150)
y=150
for i in range(0,8):
    if i%2!=0  :
        for x in range(-200,200,100):
            turtle.goto(x,y)
            turtle.color("black")
            turtle.begin_fill()
            for s in range(4):
                turtle.forward(50)
                turtle.left(90)
            turtle.end_fill()
    else:
        for x in range(-150,250,100):
            turtle.goto(x,y)
            turtle.color("black")
            turtle.begin_fill()
            for s in range(4):
                turtle.forward(50)
                turtle.left(90)
            turtle.end_fill()
    y=y-50

turtle.hideturtle()
turtle.done()