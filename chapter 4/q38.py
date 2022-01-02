import turtle
x1,y1,w1,h1 = eval(input("Enter center(x,y) width and height (w,h) of rectangle 1 : "))
x2,y2,w2,h2 = eval(input("Enter center(x,y) width and height (w,h) of rectangle 2 : "))
maxx = x1 if (w1>w2 and  h1>h2) else x2
maxy = y1 if (w1>w2 and  h1>h2) else y2
minx = x2 if (w1>w2 and  h1>h2) else x1
miny = y2 if (w1>w2 and  h1>h2) else y1

bigRect = 'r1' if (w1>w2 and  h1>h2) else 'r2'
smallRect = 'r2' if (w1>w2 and  h1>h2) else 'r1'

turtle.penup()
turtle.goto(((x1-w1)/2),((y1-h1)/2))
turtle.pendown()
turtle.forward(w1)
turtle.left(90)
turtle.forward(h1)
turtle.left(90)
turtle.forward(w1)
turtle.left(90)
turtle.forward(h1)
turtle.left(90)
turtle.penup()
turtle.goto(((x2-w2)/2),((y2-h2)/2))
turtle.pendown()
turtle.forward(w2)
turtle.left(90)
turtle.forward(h2)
turtle.left(90)
turtle.forward(w2)
turtle.left(90)
turtle.forward(h2)
turtle.left(90)
turtle.penup()
turtle.goto(-150,-200)


if (abs(x1-x2) > (w1/2+w2/2)) and (abs(y1-y2) > (h1/2+h2/2)):
    text = '{} is outside of {}'.format(smallRect,bigRect)
    
elif abs(minx-maxx)+min(w1,w2)/2 < max(w1,w2)/2 and abs(miny-maxy)+min(h1,h2)/2 < max(h1,h2)/2:
    text = '{} is inside of {}'.format(smallRect,bigRect)
else:
   text = '{} overlaps {}'.format(smallRect,bigRect)

turtle.write(text)
turtle.done()

