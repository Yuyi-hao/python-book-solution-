import turtle
def drawLine(x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)

# Write a string s at a location (x,y)
def writeText(s,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(s)

# draw a point at a specified location (x,y)
def drawpoint(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(6,'black') # here we use dot methode in original it is done by making a solid circle 

def drawCircle(x=0,y=0,radius = 10):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius)

def drawRectangle(x=0, y=0, width=10, height=10):
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)