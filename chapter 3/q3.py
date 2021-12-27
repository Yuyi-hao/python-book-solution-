# Geometry : estimate areas 

# importing math module 
import math

# Getting GPS location for 
Atlanta_GeorgiaX,Atlanta_GeorgiaY = 33.753746, -84.386330
Orlando_FloridaX, Orlando_FloridaY = 28.538330,-81.378883
Savannah_GeorgiaX, Savannah_GeorgiaY  = 32.080898,-81.091202
Charlotte_NorthCarolinaX,Charlotte_NorthCarolinaY =35.223789, -80.841141

RADIUS= 6371.01

# Atlanta_Georgia and Orlando_Florida
d1 = abs(RADIUS * math.acos(math.sin(math.radians(Atlanta_GeorgiaX))* math.sin(math.radians(Orlando_FloridaX)) + math.cos(math.radians(Atlanta_GeorgiaX)) * math.cos(math.radians(Orlando_FloridaX)) * math.cos(math.radians(Atlanta_GeorgiaY-Orlando_FloridaY))))

# Orlando_Florida and Savannah_Georgia
d2 = abs(RADIUS * math.acos(math.sin(math.radians(Orlando_FloridaX))* math.sin(math.radians(Savannah_GeorgiaX)) + math.cos(math.radians(Orlando_FloridaX)) * math.cos(math.radians(Savannah_GeorgiaX)) * math.cos(math.radians(Orlando_FloridaY-Savannah_GeorgiaY))))

# Atlanta_Georgia and Savannah_Georgia
d3 = abs(RADIUS * math.acos(math.sin(math.radians(Atlanta_GeorgiaX))* math.sin(math.radians(Savannah_GeorgiaX)) + math.cos(math.radians(Atlanta_GeorgiaX)) * math.cos(math.radians(Savannah_GeorgiaX)) * math.cos(math.radians(Atlanta_GeorgiaY-Savannah_GeorgiaY))))

# Savannah_Georgia and Charlotte_NorthCarolina
d4 = abs(RADIUS * math.acos(math.sin(math.radians(Savannah_GeorgiaX))* math.sin(math.radians(Charlotte_NorthCarolinaX)) + math.cos(math.radians(Savannah_GeorgiaX)) * math.cos(math.radians(Charlotte_NorthCarolinaX)) * math.cos(math.radians(Savannah_GeorgiaY-Charlotte_NorthCarolinaY))))

# Charlotte_NorthCarolina and Orlando_Florida
d5 = abs(RADIUS * math.acos(math.sin(math.radians(Charlotte_NorthCarolinaX))* math.sin(math.radians(Orlando_FloridaX)) + math.cos(math.radians(Charlotte_NorthCarolinaX)) * math.cos(math.radians(Orlando_FloridaX)) * math.cos(math.radians(Charlotte_NorthCarolinaY-Orlando_FloridaY))))

# deviding these four locations into two triangles 
# first triangle : Atlanta_Georgia, Orlando_Florida and Savannah_Georgia
s1 = (d1+d2+d3)/2
area1 = ((s1-d1)**2 + (s1-d2)**2 + (s1-d3)**2 )**0.5
# first triangle : Charlotte_NorthCarolina , Orlando_Florida and Savannah_Georgia
s2 = (d4+d2+d5)/2
area2 = ((s2-d4)**2 + (s2-d2)**2 + (s2-d5)**2 )**0.5

totalArea = area1+area2 

print('The area of these four city (Atlanta_Georgia, Orlando_Florida,Charlotte_NorthCarolina and Savannah_Georgia)is {:.4f} square kilometer'.format(totalArea))