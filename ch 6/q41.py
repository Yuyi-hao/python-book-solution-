import turtle
import listing14
import random 
def main():
    listing14.drawRectangle(-75, 0, 100, 100)
    listing14.drawCircle(50, 0, 50)
    turtle.speed(5)
    for i in range(10):
        listing14.drawpoint(random.randint(-115,-30), random.randint(-50,40))
        listing14.drawpoint(random.randint(20, 90), random.randint(-40, 25))
    turtle.done()
main()