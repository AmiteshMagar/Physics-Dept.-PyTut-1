def fact(n):
    i = n
    fac = 1
    while i>1:
        fac = fac * i
        i = i-1
    return fac

def cosfun(x,n):
    p = (-1)**n
    c = 2*n
    rest = (x**c)
    rest = p * (rest/fact(c))
    return (rest)
def sinfun(x,n):
    c = 2*n - 1
    p = (-1)**(n+1)
    rest = (x)**(c)
    rest =p *(rest/fact(c))
    return (rest)
def cosX(N,x):
    su = 0
    for n in range(0,N+1):
        su = su + cosfun(x,n)
    return su

def sinX(N,x):
    su = 0
    for n in range(1,N+1):
        su = su + sinfun(x,n)
    return su
N=(5,10,20)
x = (0,0.25,0.5,0.75)
for k in N:
    for j in x:
        print(cosX(k,j))
        print(sinX(k,j))
        
