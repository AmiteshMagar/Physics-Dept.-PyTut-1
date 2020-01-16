N=(100,200,500,1000)
for j in N:
    f=0
    for n in range(1,j):
        c= (-1)**n
        f = f+ (c/n)
    print(f)

for k in N:
    f =0
    for n in range(1,k):
        m = n * (n+1)
        f = f + (1/m)
    print(f)
