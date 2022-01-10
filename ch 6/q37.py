import random
import turtle
def printCharacter(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(chr(random.randint(67,90)).lower())

def main():
    x = -50
    y = 50
    count = 0
    for i in range(100):
        if count%15 == 0:
            x = -50
            y -=15
        printCharacter(x,y)
        x += 10
        count +=1
    turtle.done()
main()
