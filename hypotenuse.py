# This was an assignment. These functions call one another to do simple
# geometry caluclations

import math

def absolute_value(x):
    x = x/1
    if x >= 0:
        return x
    if x < 0:
        return -x
    
def hypotenuse(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

def distance(xa, ya, xb, yb):
    dx = absolute_value(xb - xa)
    dy = absolute_value(yb - ya)
    d = hypotenuse(dx,dy)
    return d

def area_circle(radius):
    area = math.pi*(radius**2)
    return area

def area_circle2(xc, yc, xp, yp):
    radius = distance(xc,yc,xp,yp)
    area = area_circle(radius)
    return area






