import turtle

x0,y0 = eval(input("Enter Coordinates of point 0 : "))
x1,y1 = eval(input("Enter Coordinates of point 1 : "))
x2,y2 = eval(input("Enter Coordinates of point 2 : "))

position = (x1 - x0)*(y2 - y0) -  (x2 - x0)*(y1 - y0) 



turtle.penup()
turtle.goto(x0,y0)
turtle.pendown()
turtle.write(' p0({}, {})'.format(x0,y0))
turtle.penup()
turtle.goto(x0,y0)
turtle.pendown()
turtle.goto(x1,y1)
turtle.write(' p1({}, {})'.format(x1,y1))
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.dot(6,'red')
turtle.write(' p2({}, {})'.format(x2,y2))

if position != 0:
    if position > 0 :
        positionOfPoint = 'left'
    elif position <0:
        positionOfPoint = 'right'
    turtle.penup()
    turtle.goto(x2-200,y2-10)
    turtle.pendown()
    turtle.write("p2 is on {} side of the line from p0 to p1".format(positionOfPoint))
    print("p2({},{}) is on {} side of the line from p0({},{}) to p1({},{})".format(x2,y2,positionOfPoint,x0,y0,x1,y1))
    turtle.done()
else:
    turtle.penup()
    turtle.goto(x2-100,y2-10)
    turtle.pendown()
    turtle.write("p2 is on the line from p0 to p1")
    print("p2({},{}) is on the line from p0({},{}) to p1({},{})".format(x2,y2,x0,y0,x1,y1))
    turtle.done()