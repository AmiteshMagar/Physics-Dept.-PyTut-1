import math
ls =[]
print("Enter the sides of the triangle")
for i in range(3):
    ls.append(float(input()))

def cosform(a,b,c):
    num = a**2 + b**2 - c**2
    den = 2*a*b
    frac = num/den
    return frac
angles=[]
for i in range(3):
    val= cosform(ls[0],ls[1],ls[2])
    angles.append(math.acos(val))
    ls[0],ls[1],ls[2]=ls[1],ls[2],ls[0]
print(angles)
