x1,y1,x2,y2 = eval(input("Enter the end point is line 1 :"))
x3,y3,x4,y4 = eval(input("Enter the end point is line 2 :"))

a1 = y1-y2
b1 = x2-x1
c1 = (y1-y2)*x1 - (x1-x2)*y1
a2 = y3-y4
b2 = x4-x3
c2 = (y3-y4)*x3 - (x3-x4)*y3

if a1/a2 == b1/b2 and b1/b2 != c1/c2:
    print("The lines are parallel and no solution exist")
elif  a1/a2 == b1/b2 and b1/b2 == c1/c2:
    print("The lines are overlaps eachother and no unique solution exist")
else:
    x = ((b2*c1) - (b1*c2))/((a1*b2) - (b1*a2))
    y = ((a1*c2) - (c1*a2))/((a1*b2) - (b1*a2))
    print('The intersecting point is at ({:.4f}, {:.4f})'.format(x,y))

   