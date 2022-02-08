from tkinter import * 
import math 
import random
class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self,x):
        self.__x = x
        return self.__x
    def setY(self,y):
        self.__y = y 
        return self.__y

    def distance(self, point):
        d = ((self.__x-point.getX())**2+(self.__y-point.getY())**2)**0.5
        return d
    def isNear(self,point):
        d = self.distance(point)
        if d<5:
            return True
        else:
            return False
    def __str__(self):
        return '( ' + str(self.__x) + ',' + str(self.__y) + ' )'

class IntersectingPoint:
    def __init__(self):
        window = Tk()
        window.title("Intersecting point")
        self.canvas = Canvas(window,width = 500,height = 500,bg = "white")
        self.canvas.pack()
        self.va = Point(random.randint(0,450),random.randint(0,450))
        self.vb = Point(random.randint(0,450),random.randint(0,450))
        self.vc = Point(random.randint(0,450),random.randint(0,450))
        

        self.canvas.create_line(self.va.getX(),self.va.getY(),self.vb.getX(),self.vb.getY(),tags="line1")
        self.canvas.create_line(self.va.getX(),self.va.getY(),self.vc.getX(),self.vc.getY(),tags="line2")
        self.canvas.create_line(self.vc.getX(),self.vc.getY(),self.vb.getX(),self.vb.getY(),tags="line3")

        a = math.sqrt((self.vb.getX() - self.vc.getX()) * (self.vb.getX() - self.vc.getX()) + (self.vb.getY() - self.vc.getY()) * (self.vb.getY() - self.vc.getY())) 
        b = math.sqrt((self.va.getX() - self.vc.getX()) * (self.va.getX() - self.vc.getX()) + (self.va.getY() - self.vc.getY()) * (self.va.getY() - self.vc.getY()))
        c = math.sqrt((self.va.getX() - self.vb.getX()) * (self.va.getX() - self.vb.getX()) + (self.va.getY() - self.vb.getY()) * (self.va.getY() - self.vb.getY()))

        A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c))) 
        B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
        C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

        self.canvas.create_text(self.va.getX(),self.va.getY(),text='{:.2f}'.format(A),tags="text")
        self.canvas.create_text(self.vb.getX(),self.vb.getY(),text='{:.2f}'.format(B),tags="text")
        self.canvas.create_text(self.vc.getX(),self.vc.getY(),text='{:.2f}'.format(C),tags="text")


        self.canvas.bind("<B1-Motion>",self.movingPoints)
        self.canvas.bind("<ButtonRelease>",self.resetCursor)

        window.mainloop()

    def movingPoints(self,event):
        self.canvas.delete("line1")
        self.canvas.delete("line2")
        self.canvas.delete("line3")
        self.canvas.delete("text")
        point = Point(event.x,event.y)

        if self.va.isNear(point):
            self.va.setX(event.x)
            self.va.setY(event.y)
            self.canvas.config(cursor="crosshair")
        elif self.vb.isNear(point):
            self.vb.setX(event.x)
            self.vb.setY(event.y)
            self.canvas.config(cursor="crosshair")
        elif self.vc.isNear(point):
            self.vc.setX(event.x)
            self.vc.setY(event.y)
            self.canvas.config(cursor="crosshair")

        
        self.canvas.create_line(self.va.getX(),self.va.getY(),self.vb.getX(),self.vb.getY(),tags="line1")
        self.canvas.create_line(self.va.getX(),self.va.getY(),self.vc.getX(),self.vc.getY(),tags="line2")
        self.canvas.create_line(self.vc.getX(),self.vc.getY(),self.vb.getX(),self.vb.getY(),tags="line3")

        a = math.sqrt((self.vb.getX() - self.vc.getX()) * (self.vb.getX() - self.vc.getX()) + (self.vb.getY() - self.vc.getY()) * (self.vb.getY() - self.vc.getY())) 
        b = math.sqrt((self.va.getX() - self.vc.getX()) * (self.va.getX() - self.vc.getX()) + (self.va.getY() - self.vc.getY()) * (self.va.getY() - self.vc.getY()))
        c = math.sqrt((self.va.getX() - self.vb.getX()) * (self.va.getX() - self.vb.getX()) + (self.va.getY() - self.vb.getY()) * (self.va.getY() - self.vb.getY()))

        A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c))) 
        B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
        C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))
        self.canvas.create_text(self.va.getX(),self.va.getY(),text='{:.2f}'.format(A),tags="text")
        self.canvas.create_text(self.vb.getX(),self.vb.getY(),text='{:.2f}'.format(B),tags="text")
        self.canvas.create_text(self.vc.getX(),self.vc.getY(),text='{:.2f}'.format(C),tags="text")


    def resetCursor(self,event):
        self.canvas.config(cursor="arrow")


IntersectingPoint()