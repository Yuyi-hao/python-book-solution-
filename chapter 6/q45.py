import turtle
def drawPolygon(x=0, y=0, radius=50, numberOfSides=3):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius,360,numberOfSides)
    turtle.done()
def main():
    x = -160
    y = 0
    radius = 25
    for i in range(3,9):
        drawPolygon(x,y,radius,numberOfSides=i)
        x += 2*radius+5
main()