x1,y1,r1 = eval(input("Enter center(x,y) and radius of the circle 1 : "))
x2,y2,r2 = eval(input("Enter center(x,y) and radius of the circle 2 : "))
maxx = x1 if(r1>r2) else x2
minx = x2 if(r1>r2) else x1
maxy = y1 if(r1>r2) else y2
miny = y2 if(r1>r2) else y1
maxc = 'c1' if(r1>r2) else 'c2'
minc = 'c2' if(r1>r2) else 'c1'

# determine the distance between centers of two circle

d = ((x1-x2)**2 + (y2-y1)**2)**0.5
print(d)
print(max(r1,r2),d+2*(min(r1,r2)))

if d > r1+r2:
    print('{} is outside of {}'.format(minc,maxc))
elif max(r1,r2) > d+(min(r1,r2)):
    print('{} is inside of {}'.format(minc,maxc))
else:
    print('{} overlaps {}'.format(minc,maxc))


