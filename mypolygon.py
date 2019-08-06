
#   This was a textbook project. The goal was to write functions using
#   the turtle program that draw certain shapes and designs.
#   I don't know the official solutions, but
#   these various functions I wrote drew what they were intended to.


import math
import turtle
bob = turtle.Turtle()

print(bob)


def polygon(length,n): #This function draws polygons with n sides
    c = 360/n
    for i in range(n):
        bob.fd(length)
        bob.lt(c)

def circle(r): #This function draws circles with radius r
    d = (2*math.pi*r)/360
    polygon(d,360)

def basic_arc(r,angle): #This function draws an arc
    n = float(r*angle*(math.pi/180))
    s = 0
    i = angle/n
    while s < n:
        bob.fd(1)
        bob.lt(i)
        s += 1
        continue
    
def arc_seg(r,angle): #This function draws an arc segment (not an assignment)
    bob.fd(r)
    bob.lt(90)
    basic_arc(r,angle)
    bob.lt(90)
    bob.fd(r)  

def pizza(r,angle,c): #This funtion was part of a different project
    n = float(r*angle*(math.pi/180))
    i = angle/n
    while True:
        s = 0
        arc(r,angle)
        if s>= n:
            bob.lt(c)
            continue

def petals(a,c,n): #This function draws symetrical petal patterns 
    b = 180-(c/2)
    i = 0
    while i < n:
        n = float(a*c*(math.pi/180))
        s = 0
        i = c/n
        while s < n:
            bob.fd(1)
            bob.lt(i)
            s += 1
            continue
        bob.lt(b)
        i += 1
        continue

def triangles(length,angle): #This function draws a polygon made of triangles
    deg = angle*(math.pi/180)
    a = math.pi - (2*deg)
    b = (length*math.sin(a))/(math.sin(deg))
    c = 180 - angle
    while True:
        bob.fd(length)
        bob.rt(c)
        bob.fd(b)
        bob.rt(c)
        bob.fd(length)
        bob.rt(180)
        continue

def spiral(a,angle): #This function draws a spiral
    c = 360
    while True:
        r = a/angle
        d = (2*math.pi*r)/c
        bob.fd(1)
        bob.lt(d)
        a += 1
        c -= 1
        if c == 1:
            break
        continue



    
def letter_a(): #This function draws the letter A
    bob.lt(70)
    bob.fd(100)
    bob.rt(140)
    bob.fd(50)
    bob.rt(110)
    bob.fd(35)
    bob.rt(180)
    bob.fd(35)
    bob.rt(70)
    bob.fd(50)
    bob.lt(70)
    bob.fd(10)


def letter_b():#Letter B (adjustments needed to basic_arc to work)
    bob.lt(90)
    bob.fd(94)
    bob.rt(90)
    basic_arc(23,180)
    bob.lt(180)
    bob.fd(10)
    basic_arc(24,180)
    bob.fd(10)
    bob.lt(183.3)
    bob.fd(43)
    
def letter_c(): #Letter C (adjustments needed to basic_arc to work)
    bob.fd(57)
    bob.rt(180)
    bob.fd(10)
    basic_arc(47,180)
    bob.fd(20)

def letter_d(): #Letter D (adjustments needed to basic_arc to work)
    bob.fd(10)
    basic_arc(47,180)
    bob.fd(10)
    bob.rt(89.5)
    bob.fd(94)
    bob.rt(180)
    bob.fd(94)
    bob.lt(90)
    bob.fd(67)

    
#polygon(100,7)

#circle(100)
    
#basic_arc(100,90)

#arc_seg(100,60)

#petals(100,60,200)

#triangles(100,70)

#spiral(1000,60)


    
#turtle.mainloop()

