x0,y0 = eval(input("Enter Coordinates of point 0 : "))
x1,y1 = eval(input("Enter Coordinates of point 1 : "))
x2,y2 = eval(input("Enter Coordinates of point 2 : "))

position = (x1 - x0)*(y2 - y0) -  (x2 - x0)*(y1 - y0) 
d = round(((x0-x1)**2 + (y0-y1)**2)**0.5)
d1 = round(((x0-x2)**2 + (y0-y2)**2)**0.5)
d2 = round(((x1-x2)**2 + (y1-y2)**2)**0.5)

if position != 0:
    print("p2({},{}) is not on the line from p0({},{}) to p1({},{})".format(x2,y2,x0,y0,x1,y1))
else:
    if d == d1+d2: 
        print("p2({},{}) is on the line from p0({},{}) to p1({},{})".format(x2,y2,x0,y0,x1,y1))
    else:
        print("p2({},{}) is not on the line from p0({},{}) to p1({},{})".format(x2,y2,x0,y0,x1,y1))