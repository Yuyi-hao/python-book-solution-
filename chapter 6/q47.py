import turtle
def drawChessboard(startX,endX,startY,endY):
    turtle.speed(10)
    side = abs(startX-endX)/8
    height = abs(endY-startY)
    width = abs(startX-endX)
    x = startX +side
    y = startY-side
    turtle.penup()
    turtle.goto(startX-1,endY-1)
    turtle.pendown()
    # creating border
    turtle.forward(width+1)
    turtle.left(90)
    turtle.forward(height+1)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    # making blocks on board 
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(0,8,1):
        x = startX
        if i%2 !=0:
            turtle.penup()
            turtle.goto(x,y) 
            turtle.pendown()
            for k in range(0,4,1):
                turtle.begin_fill()
                for j in range(0,4):
                    turtle.forward(side)
                    turtle.left(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(2*side)
                turtle.pendown()
                x = x+side*2
        else:
            x = x+side
            turtle.penup()
            turtle.goto(x,y) 
            turtle.pendown()
            for k in range(0,4,1):
                turtle.begin_fill()
                for j in range(0,4):
                    turtle.forward(side)
                    turtle.left(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(2*side)
                turtle.pendown()
                x = x+side*2
        y = y-side
    
            

    
def main():
    startX,startY = eval(input("Enter the starting x,y : "))
    endX,endY = eval(input("Enter the ending x,y : "))
    drawChessboard(startX,endX,startY,endY)
    drawChessboard(endX+(abs(startX-endX)/8),endX+(abs(startX-endX)),startY,endY)
    turtle.done()
main()



