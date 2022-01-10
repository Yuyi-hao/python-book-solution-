import turtle
def drawLine(x1,y1,x2,y2,color = 'black', size = 1):
    turtle.penup()
    turtle.pensize(size)
    turtle.color(color)
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.penup()

def main():
    x1,y1 = eval(input("Enter the starting point (x1,y1) : "))
    x2,y2 = eval(input("Enter the ending point (x2,y2) : "))
    color = input("Enter the color : ").lower()
    size = int(input("Enter the size (1-10) : "))
    drawLine(x1,y1,x2,y2,color, size)
    turtle.done()

main()