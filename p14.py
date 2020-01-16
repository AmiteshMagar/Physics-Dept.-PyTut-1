import math
print("lengths    time")
for l in range(1,13):
    f = 2* math.pi * math.sqrt(l/9.81)
    print(str(l)+"    "+str(f))
    
