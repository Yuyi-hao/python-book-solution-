import turtle
def hexagon(x,y,side):
    turtle.penup()
    turtle.goto(x,y)
    turtle.left(60)
    turtle.pendown()
    for i in range(6):
        for i in range(3):
            turtle.forward(side)
            turtle.right(120)
        turtle.forward(side)
        turtle.right(60)
    turtle.right(60)

def triangle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.right(120)

def main():
    hexagon(-100,0,100)
    turtle.left(30)
    triangle(174)
    turtle.left(30)
    turtle.forward(100)
    turtle.right(90)
    triangle(174)
    turtle.done()
main()



