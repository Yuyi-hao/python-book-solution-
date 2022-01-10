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
    drawLine(-100,0,100,0)
    drawLine(100,0,-62,-119)
    drawLine(-62,-119,0,75)
    drawLine(0,75,62,-119)
    drawLine(62,-119,-100,0)
    turtle.done()
main()