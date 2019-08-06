#   This was my first program.


a = float(input("Enter the coefficient of the second degree variable:"))
b = float(input("Enter the coefficient of the first degree variable:"))
c = float(input("Enter the constant:"))

root =((b**2)-4*a*c)
if root < 0:
    print("Domain Error")
    
else:
    d = root**0.5
    e = 2*a
    f = -b/e
    g = d/e
    pos = str(float(f+g))
    neg = str(float(f-g))
    print("x = " + pos)
    print("x = " + neg)


print("Program End")





      
