def leftOfTheLine(x0,y0,x1,y1,x2,y2):
    position = (x1 - x0)*(y2 - y0) -  (x2 - x0)*(y1 - y0) 
    if position != 0:
        if position > 0 :
            return True
        else:
            return False
    else:
        return False

def rightOfTheLine(x0,y0,x1,y1,x2,y2):
    position = (x1 - x0)*(y2 - y0) -  (x2 - x0)*(y1 - y0) 
    if position != 0:
        if position < 0 :
            return True
        else:
            return False
    else:
        return False

def OnTheSameLine(x0,y0,x1,y1,x2,y2):
    position = (x1 - x0)*(y2 - y0) -  (x2 - x0)*(y1 - y0) 
    if position == 0:
        return True
    else:
        return False

def onTheLineSegment(x0,y0,x1,y1,x2,y2):
    position = (x1 - x0)*(y2 - y0) -  (x2 - x0)*(y1 - y0)
    d1 = ((x1 - x2)**2 - (y1 - y2)**2)**0.5
    d2 = ((x0 - x2)**2 - (y0 - y2)**2)**0.5
    d  = ((x0 - x1)**2 - (y0 - y1)**2)**0.5
    if position == 0:
        if(d == d1+d2):
            return True
        else:
            return False
    else:
        return False

def main():
    x0,y0 = eval(input("Enter Coordinates of point 0 : "))
    x1,y1 = eval(input("Enter Coordinates of point 1 : "))
    x2,y2 = eval(input("Enter Coordinates of point 2 : "))
    if leftOfTheLine(x0,y0,x1,y1,x2,y2):
        print('The point p2 is left side of line form p0 to p1')
    elif rightOfTheLine(x0,y0,x1,y1,x2,y2):
        print('The point p2 is right side of line form p0 to p1')
    elif onTheLineSegment(x0,y0,x1,y1,x2,y2):
        print('The point p2 is on the  line segment  form p0 to p1')
    elif OnTheSameLine(x0,y0,x1,y1,x2,y2):
        print('The point p2 is on the line form p0 to p1')

main()

