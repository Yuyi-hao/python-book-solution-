x0,y0 = eval(input("Enter Coordinates of point 0 : "))
x1,y1 = eval(input("Enter Coordinates of point 1 : "))
x2,y2 = eval(input("Enter Coordinates of point 2 : "))

position = (x1 - x0)*(y2 - y0) -  (x2 - x0)*(y1 - y0) 

if position != 0:
    if position > 0 :
        positionOfPoint = 'left'
    elif position <0:
        positionOfPoint = 'right'
    print("p2({},{}) is on {} side of the line from p0({},{}) to p1({},{})".format(x2,y2,positionOfPoint,x0,y0,x1,y1))
else:
    print("p2({},{}) is on the line from p0({},{}) to p1({},{})".format(x2,y2,x0,y0,x1,y1))