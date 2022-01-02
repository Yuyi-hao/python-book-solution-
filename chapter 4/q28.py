
x1,y1,w1,h1 = eval(input("Enter center(x,y) width and height (w,h) of rectangle 1 : "))
x2,y2,w2,h2 = eval(input("Enter center(x,y) width and height (w,h) of rectangle 2 : "))
maxx = x1 if (w1>w2 and  h1>h2) else x2
maxy = y1 if (w1>w2 and  h1>h2) else y2
minx = x2 if (w1>w2 and  h1>h2) else x1
miny = y2 if (w1>w2 and  h1>h2) else y1

bigRect = 'r1' if (w1>w2 and  h1>h2) else 'r2'
smallRect = 'r2' if (w1>w2 and  h1>h2) else 'r1'

if (abs(x1-x2) > (w1/2+w2/2)) and (abs(y1-y2) > (h1/2+h2/2)):
    print('{} is outside of {}'.format(smallRect,bigRect))
    
elif abs(minx-maxx)+min(w1,w2)/2 < max(w1,w2)/2 and abs(miny-maxy)+min(h1,h2)/2 < max(h1,h2)/2:
    print('{} is inside of {}'.format(smallRect,bigRect))
else:
   print('{} overlaps {}'.format(smallRect,bigRect))


# (w1<w2 or w2<w1) and (h1<h2 or h2<h1)
# 