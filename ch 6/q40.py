import turtle
def drawrectangle(color = 'black',x = 0,y = 0,width = 30,height = 30):
    turtle.penup() # Pull the pen up
    turtle.color(color)
    turtle.goto(x + width / 2, y + height / 2)
    turtle.begin_fill()
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.end_fill()
    
def drawCircle(color = 'black',x = 0,y = 0,radius = 50):
    turtle.penup()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()
def main():
    # taking input 
    rx,ry = eval(input("Enter the center of rectangle "))
    rWidth,rHeight = eval(input("Enter the width and height of rectangel : "))
    color = input('Enter the color : ').lower()
    cx,cy = eval(input("Enter the center of circle "))
    radius = eval(input("Enter the radius of circle : "))
    cColor = input('Enter the color : ').lower()

    drawCircle(cColor,cx,cy,radius)
    drawrectangle(color,rx,ry,rWidth,rHeight)
    turtle.done()
main()