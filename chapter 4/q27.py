x,y = eval(input("Enter the point (x,y) : "))

print((-1/2)*(x)+100)
if x<0 and y<0:
    print("The point({},{}) is outside the triangle ".format(x,y))
if x <200 and y <100:
    if y <= -(1/2)*(x)+100:
        print("The point({},{}) is inside the triangle ".format(x,y))
    else:
        print("The point({},{}) is outside the triangle ".format(x,y))
    
